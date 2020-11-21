import contextlib
import errno
import os
from typing import Callable
from typing import Generator


if os.name == 'nt':  # pragma: no cover (windows)
    import msvcrt

    # https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/locking

    # on windows we lock "regions" of files, we don't care about the actual
    # byte region so we'll just pick *some* number here.
    _region = 0xffff

    @contextlib.contextmanager
    def _locked(
            fileno: int,
            blocked_cb: Callable[[], None],
    ) -> Generator[None, None, None]:
        try:
            # TODO: https://github.com/python/typeshed/pull/3607
            msvcrt.locking(fileno, msvcrt.LK_NBLCK, _region)
        except OSError:
            blocked_cb()
            while True:
                try:
                    # TODO: https://github.com/python/typeshed/pull/3607
                    msvcrt.locking(fileno, msvcrt.LK_LOCK, _region)
                except OSError as e:
                    # Locking violation. Returned when the _LK_LOCK or _LK_RLCK
                    # flag is specified and the file cannot be locked after 10
                    # attempts.
                    if e.errno != errno.EDEADLOCK:
                        raise
                else:
                    break

        try:
            yield
        finally:
            # From cursory testing, it seems to get unlocked when the file is
            # closed so this may not be necessary.
            # The documentation however states:
            # "Regions should be locked only briefly and should be unlocked
            # before closing a file or exiting the program."
            # TODO: https://github.com/python/typeshed/pull/3607
            msvcrt.locking(fileno, msvcrt.LK_UNLCK, _region)
else:  # pragma: win32 no cover
    import fcntl

    @contextlib.contextmanager
    def _locked(
            fileno: int,
            blocked_cb: Callable[[], None],
    ) -> Generator[None, None, None]:
        try:
            fcntl.flock(fileno, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:  # pragma: no cover (tests are single-threaded)
            blocked_cb()
            fcntl.flock(fileno, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fileno, fcntl.LOCK_UN)


@contextlib.contextmanager
def lock(
        path: str,
        blocked_cb: Callable[[], None],
) -> Generator[None, None, None]:
    with open(path, 'a+') as f:
        with _locked(f.fileno(), blocked_cb):
            yield
