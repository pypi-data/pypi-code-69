"""This module implements the Aug class."""
import time
import uuid

from rook.logger import logger
from rook.user_warnings import UserWarnings
from rook.processor.error import Error
from rook.processor.namespaces.container_namespace import ContainerNamespace
from rook.processor.namespaces.stack_namespace import StackNamespace
from rook.processor.namespaces.python_utils_namespace import PythonUtilsNamespace
from rook.processor.namespaces.trace_namespace import TraceNamespace
from rook.processor.namespaces.noop_namespace import NoopNamespace
from rook.exceptions import RookRuleMaxExecutionTimeReached, RookRuleRateLimited
from rook.augs.aug_rate_limiter import AugRateLimiter


class Aug(object):
    """The Aug class is the skeleton that holds together all the components that define a modification to the application.

    This class brings together the following elements:
    - location - specifies when to run the modification.
    - extractor - specifies attributes to extract from the application's state before evaluating the modification.
    - condition - specifies an optional filter as to when to run the modification.
    - action - specifies the modification to preform.
    """

    def __init__(self, aug_id, location, extractor, condition, action, output, max_aug_execution_time=0, rate_limits=None):
        """Build an Aug object from the individual elements."""
        self.aug_id = aug_id
        self._location = location
        self._extractor = extractor
        self._condition = condition
        self._action = action
        self._output = output
        self._max_aug_time = max_aug_execution_time
        self._enabled = True

        if rate_limits:
            self._rate_limiter = AugRateLimiter(rate_limits[0], rate_limits[1])
        else:
            self._rate_limiter = AugRateLimiter(None, None)

        self._status = None
        self._warningCache = {}
        self._logCache = {}

    def add_aug(self, trigger_services):
        """Use the location to add the Aug to the relevant trigger service."""
        try:
            self._location.add_aug(trigger_services, self._output, self)
        except Exception as exc:
            message = "Exception when adding aug"
            logger.exception(message + " " + self.aug_id + " : " + str(exc))
            self.set_error(Error(exc=exc, message=message))

    def execute(self, frame_namespace, extracted):
        """Called by the trigger service to run the extractor, condition and action."""
        if not self._enabled:
            return

        now = time.time()
        limit_key = None
        executed = False

        try:
            with UserWarnings(self):
                if self._extractor:
                    self._extractor.execute(frame_namespace, extracted)

                store = ContainerNamespace({})

                namespace = ContainerNamespace({
                    'frame': frame_namespace,
                    'stack': StackNamespace(frame_namespace),
                    'extracted': ContainerNamespace(extracted),
                    'store': store,
                    'temp': ContainerNamespace({}),
                    'python': PythonUtilsNamespace(),
                    'utils': PythonUtilsNamespace(),
                    'trace': TraceNamespace(),
                    'state': NoopNamespace()
                })

                if not self._condition or self._condition.evaluate(namespace, extracted):
                    limit_key = self._rate_limiter.allow(now)

                    if limit_key is None:
                        self.send_warning(Error(RookRuleRateLimited()))
                        return

                    executed = True
                    msg_id = uuid.uuid4().hex

                    logger.info("Executing aug-\t%s (msg ID %s)", self.aug_id, msg_id)
                    self._action.execute(self.aug_id, msg_id, namespace, self._output)

        # Don't stop test exceptions from propagating
        except AssertionError:
            raise
        # Catch and silence everything else
        except Exception as exc:
            message = "Exception while processing Aug"
            rook_error = Error(exc=exc, message=message)

            if not self._should_silence_log(rook_error, self._logCache):
                logger.exception(message)

            self.send_warning(rook_error)
        finally:
            if executed:
                duration = time.time() - now

                if 0 < self._max_aug_time < duration * 1000:
                    self.set_error(Error(exc=RookRuleMaxExecutionTimeReached()))
                    self._enabled = False

                if limit_key:
                    self._rate_limiter.record(limit_key, duration)

    def set_active(self):
        self._send_rule_status("Active")

    def set_pending(self):
        self._send_rule_status("Pending")

    def set_removed(self):
        self._send_rule_status("Deleted")

    def set_error(self, error):
        self._send_rule_status("Error", error)

    def set_unknown(self, error):
        self._send_rule_status("Unknown", error)

    def send_warning(self, error):
        if self._should_silence_log(error, self._warningCache):
            return

        logger.warning(error.message)

        self._output.send_warning(self.aug_id, error)

    def _send_rule_status(self, status, error=None):
        if self._status == status:
            return

        logger.info("Updating rule status for %s to %s", self.aug_id, status)

        self._status = status
        self._output.send_rule_status(self.aug_id, status, error)

    def _should_silence_log(self, error, log_cache):
        if error.message in log_cache or len(log_cache) >= 10:
            return True

        log_cache[error.message] = True

        return False
