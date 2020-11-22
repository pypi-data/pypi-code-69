import inspect
from collections import OrderedDict
from typing import List, Any, Sequence, Callable, Optional

from lemoncheesecake.helpers.moduleimport import import_module, get_matching_files, get_py_files_from_dir
from lemoncheesecake.exceptions import FixtureConstraintViolation, ModuleImportError, FixtureLoadingError
from lemoncheesecake.helpers.orderedset import OrderedSet
from lemoncheesecake.helpers.introspection import get_callable_args


_FORBIDDEN_FIXTURE_NAMES = ("fixture_name",)
_SCOPE_LEVELS = {
    "test": 1,
    "suite": 2,
    "session": 3,
    "pre_run": 4
}

_scheduled_fixtures = None  # type: Optional[ScheduledFixtures]


def initialize_fixture_cache(scheduled_fixtures):
    global _scheduled_fixtures
    _scheduled_fixtures = scheduled_fixtures


def get_fixture(name):
    """
    Return the corresponding fixture value. Only fixtures whose scope is 'pre_run' can be retrieved.
    """
    global _scheduled_fixtures

    assert _scheduled_fixtures, "Fixture cache has not yet been initialized"
    if not _scheduled_fixtures.has_fixture(name):
        raise LookupError("Fixture '%s' either does not exist or doesn't have a pre_run scope" % name)

    return _scheduled_fixtures.get_fixture_result(name)


class _FixtureInfo:
    def __init__(self, names, scope):
        self.names = names
        self.scope = scope


def fixture(names=None, scope="test"):
    """
    Decorator. Declare a function as a fixture.
    :param names: an optional list of names that can be used to access the fixture value,
        if no names are provided the decorated function name will be used
    :param scope: the fixture scope, available scopes are: "test", "suite", "session", "pre_run"; default is "test"
    """
    def wrapper(func):
        if scope not in _SCOPE_LEVELS.keys():
            raise ValueError("Invalid fixture scope '%s' in fixture function '%s'" % (scope, func.__name__))

        setattr(func, "_lccfixtureinfo", _FixtureInfo(names, scope))
        return func

    return wrapper


class _FixtureResult(object):
    def __init__(self, name, result):
        self.name = name
        if inspect.isgenerator(result):
            self._generator = result
            self._result = next(result)
        else:
            self._generator = None
            self._result = result

    def get(self):
        return self._result

    def teardown(self):
        if not self._generator:
            return

        try:
            next(self._generator)
        except StopIteration:
            pass
        else:
            raise AssertionError("Fixture '%s' yields more than once: only one yield is supported." % self.name)


class _BaseFixture(object):
    def is_builtin(self):
        return False

    def get_scope_level(self):
        return {
            "test": 1,
            "suite": 2,
            "session": 3,
            "pre_run": 4
        }[self.scope]


class Fixture(_BaseFixture):
    def __init__(self, name, func, scope, params):
        self.name = name
        self.func = func
        self.scope = scope
        self.params = params

    def execute(self, params={}):
        for param_name in params.keys():
            assert param_name in self.params

        return _FixtureResult(self.name, self.func(**params))


class BuiltinFixture(_BaseFixture):
    def __init__(self, name, value):
        self.name = name
        self.scope = "pre_run"
        self.params = []
        self._value = value

    def is_builtin(self):
        return True

    def execute(self, params={}):
        return _FixtureResult(self.name, self._value() if callable(self._value) else self._value)


class ScheduledFixtures(object):
    def __init__(self, scope, fixtures=(), parent_scheduled_fixtures=None):
        self.scope = scope
        self._fixtures = OrderedDict()
        self._parent_scheduled_fixtures = parent_scheduled_fixtures
        self._results = {}
        for fixture in fixtures:
            self.add_fixture(fixture)

    def add_fixture(self, fixture):
        assert fixture.scope == self.scope
        self._fixtures[fixture.name] = fixture

    def get_fixture_names(self):
        return self._fixtures.keys()

    def has_fixture(self, name):
        return name in self._fixtures

    def is_empty(self):
        return len(self._fixtures) == 0

    def _get_fixture_params(self, name):
        return {
            param_name: name if param_name == "fixture_name" else self.get_fixture_result(param_name)
                for param_name in self._fixtures[name].params
        }

    def _setup_fixture(self, name):
        assert name not in self._results, "Cannot setup fixture '%s', it has already been executed" % name
        self._results[name] = self._fixtures[name].execute(self._get_fixture_params(name))

    def _teardown_fixture(self, name):
        assert name in self._results, "Cannot teardown fixture '%s', it has not been previously executed" % name
        self._results[name].teardown()
        del self._results[name]

    def get_setup_teardown_pairs(self):
        return list(map(
            lambda name: (lambda: self._setup_fixture(name), lambda: self._teardown_fixture(name)),
            self._fixtures
        ))

    def get_fixture_result(self, name):
        if name in self._fixtures:
            assert name in self._results, "Cannot get fixture '%s' result, it has not been previously executed" % name
            return self._results[name].get()
        elif self._parent_scheduled_fixtures:
            return self._parent_scheduled_fixtures.get_fixture_result(name)
        else:
            raise LookupError("Cannot find fixture named '%s' in scheduled fixtures" % name)

    def get_fixture_results(self, names):
        return {name: self.get_fixture_result(name) for name in names}


class FixtureRegistry:
    def __init__(self):
        self._fixtures = {}

    def add_fixture(self, fixture):
        if fixture.name in self._fixtures and self._fixtures[fixture.name].is_builtin():
            raise FixtureConstraintViolation("'%s' is a builtin fixture name" % fixture.name)
        self._fixtures[fixture.name] = fixture

    def add_fixtures(self, fixtures):
        for fixture in fixtures:
            self.add_fixture(fixture)

    def get_fixture(self, name):
        return self._fixtures[name]

    def get_fixture_dependencies(self, name, ref_fixtures=()):
        fixture_params = [p for p in self._fixtures[name].params if p != "fixture_name"]
        if any(ref_fixture in fixture_params for ref_fixture in ref_fixtures):
            raise FixtureConstraintViolation(
                "Fixture params %s have circular dependency on a fixture among %s" % (fixture_params, ref_fixtures)
            )

        dependencies = OrderedSet()
        for param in fixture_params:
            if param not in self._fixtures:
                raise FixtureConstraintViolation("Fixture '%s' used by fixture '%s' does not exist" % (param, name))
            dependencies.update(self.get_fixture_dependencies(param, (name,) + ref_fixtures))
        dependencies.update(fixture_params)

        return dependencies

    def check_dependencies(self):
        """
        Checks for:
        - missing dependencies
        - circular dependencies
        - scope incoherence
        - forbidden fixture name
        raises FixtureConstraintViolation if a check fails
        """
        # first, check for forbidden fixture name
        for fixture_name in self._fixtures.keys():
            if fixture_name in _FORBIDDEN_FIXTURE_NAMES:
                raise FixtureConstraintViolation("Fixture name '%s' is forbidden" % fixture_name)

        # second, check for missing & circular dependencies
        for fixture_name in self._fixtures.keys():
            self.get_fixture_dependencies(fixture_name)

        # third, check fixture scope compliance with their direct fixture dependencies
        for fixture in self._fixtures.values():
            dependency_fixtures = [self._fixtures[param] for param in fixture.params if param != "fixture_name"]
            for dependency_fixture in dependency_fixtures:
                if dependency_fixture.get_scope_level() < fixture.get_scope_level():
                    raise FixtureConstraintViolation("Fixture '%s' with scope '%s' is incompatible with scope '%s' of fixture '%s'" % (
                        fixture.name, fixture.scope, dependency_fixture.scope, dependency_fixture.name
                    ))

    def check_fixtures_in_test(self, test):
        for fixture in test.get_fixtures():
            if fixture not in self._fixtures:
                raise FixtureConstraintViolation("Unknown fixture '%s' used in test '%s'" % (fixture, test.path))

    def check_fixtures_in_suite(self, suite):
        for fixture in suite.get_fixtures():
            if fixture not in self._fixtures:
                raise FixtureConstraintViolation("Suite '%s' uses an unknown fixture '%s'" % (suite.path, fixture))
            if self._fixtures[fixture].get_scope_level() < _SCOPE_LEVELS["suite"]:
                raise FixtureConstraintViolation("Suite '%s' uses fixture '%s' which has an incompatible scope" % (
                    suite.path, fixture
                ))

        for test in suite.get_tests():
            self.check_fixtures_in_test(test)

        for sub_suite in suite.get_suites():
            self.check_fixtures_in_suite(sub_suite)

    def check_fixtures_in_suites(self, suites):
        for suite in suites:
            self.check_fixtures_in_suite(suite)

    def get_fixture_scope(self, name):
        return self._fixtures[name].scope

    @staticmethod
    def get_fixtures_used_in_suite(suite, include_disabled):
        if not suite.has_enabled_tests() and not include_disabled:
            return OrderedSet()

        fixtures = suite.get_fixtures()

        for test in suite.get_tests():
            if test.is_enabled() or include_disabled:
                fixtures.update(test.get_fixtures())

        return fixtures

    @staticmethod
    def get_fixtures_used_in_suite_recursively(suite, include_disabled):
        fixtures = FixtureRegistry.get_fixtures_used_in_suite(suite, include_disabled)

        for sub_suite in suite.get_suites():
            fixtures.update(FixtureRegistry.get_fixtures_used_in_suite_recursively(sub_suite, include_disabled))

        return fixtures

    def get_scheduled_fixtures_for_scope(self, direct_fixtures, scope, parent_scheduled_fixtures=None):
        fixtures = OrderedSet()

        for fixture in direct_fixtures:
            fixtures.update(self.get_fixture_dependencies(fixture))
            fixtures.add(fixture)

        return ScheduledFixtures(
            scope, [self._fixtures[name] for name in fixtures if self._fixtures[name].scope == scope],
            parent_scheduled_fixtures=parent_scheduled_fixtures
        )

    def get_fixtures_scheduled_for_pre_run(self, suites, include_disabled=False):
        fixtures = OrderedSet()
        for suite in suites:
            fixtures.update(FixtureRegistry.get_fixtures_used_in_suite_recursively(suite, include_disabled))
        return self.get_scheduled_fixtures_for_scope(fixtures, "pre_run")

    def get_fixtures_scheduled_for_session(self, suites, prerun_session_scheduled_fixtures, include_disabled=False):
        fixtures = OrderedSet()
        for suite in suites:
            fixtures.update(FixtureRegistry.get_fixtures_used_in_suite_recursively(suite, include_disabled))
        return self.get_scheduled_fixtures_for_scope(fixtures, "session", prerun_session_scheduled_fixtures)

    def get_fixtures_scheduled_for_suite(self, suite, session_scheduled_fixtures, include_disabled=False):
        return self.get_scheduled_fixtures_for_scope(
            FixtureRegistry.get_fixtures_used_in_suite(suite, include_disabled), "suite", session_scheduled_fixtures
        )

    def get_fixtures_scheduled_for_test(self, test, suite_scheduled_fixtures):
        return self.get_scheduled_fixtures_for_scope(
            test.get_fixtures(), "test", suite_scheduled_fixtures
        )


def load_fixtures_from_func(func):
    # type: (Callable) -> List[Fixture]
    """
    Load a fixture from a function.
    """
    assert hasattr(func, "_lccfixtureinfo")
    names = func._lccfixtureinfo.names
    if not names:
        names = [func.__name__]
    scope = func._lccfixtureinfo.scope
    args = get_callable_args(func)
    return [Fixture(name, func, scope, args) for name in names]


def load_fixtures_from_module(mod):
    # type: (Any) -> List[Fixture]
    """
    Load fixtures from a module instance.

    .. versionadded:: 1.5.1
    """
    fixtures = []
    for sym_name in dir(mod):
        sym = getattr(mod, sym_name)
        if hasattr(sym, "_lccfixtureinfo"):
            fixtures.extend(load_fixtures_from_func(sym))

    return fixtures


def load_fixtures_from_file(filename):
    # type: (str) -> List[Fixture]
    """
    Load fixtures from a given file.
    """
    try:
        mod = import_module(filename)
    except ModuleImportError as e:
        raise FixtureLoadingError(str(e))

    return load_fixtures_from_module(mod)


def load_fixtures_from_files(patterns, excluding=[]):
    # type: (Any[str, Sequence[str]], Any[str, Sequence[str]]) -> List[Fixture]
    """
    Load fixtures from files.

    :param patterns: a mandatory list (a simple string can also be used instead of a single element list)
        of files to import; the wildcard '*' character can be used
    :param excluding: an optional list (a simple string can also be used instead of a single element list)
      of elements to exclude from the expanded list of files to import

    Example::

        load_fixtures_from_files("test_*.py")
    """
    fixtures = []
    for file in get_matching_files(patterns, excluding):
        fixtures.extend(load_fixtures_from_file(file))
    return fixtures


def load_fixtures_from_directory(dir):
    # type: (str) -> List[Fixture]
    """
    Load fixtures from a given directory (not recursive).
    """
    fixtures = []
    for file in get_py_files_from_dir(dir):
        fixtures.extend(load_fixtures_from_file(file))
    return fixtures
