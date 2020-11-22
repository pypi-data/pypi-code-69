import asyncio
import json
from contextlib import asynccontextmanager, suppress
from functools import partial
from typing import AsyncGenerator, Dict, Final, Hashable, Optional

json_dumps: Final = partial(json.dumps, ensure_ascii=False)


class KeyLock:
    __slots__ = ('_keys',)

    def __init__(self) -> None:
        self._keys: Final[Dict[Hashable, asyncio.Event]] = {}

    @asynccontextmanager
    async def acquire(self, key: Hashable) -> AsyncGenerator[None, None]:
        while key in self._keys:
            await self._keys[key].wait()
        self._keys[key] = asyncio.Event()
        try:
            yield
        finally:
            self._keys.pop(key).set()


class FreqLimit:
    __slots__ = ('_interval', '_clean_interval', '_events', '_ts',
                 '_clean_event', '_clean_task')

    def __init__(self, interval: float, clean_interval: float = 0) -> None:
        if interval <= 0:
            raise RuntimeError('Interval must be greater than 0')
        if clean_interval < 0:
            raise RuntimeError('Clean interval must be greater than '
                               'or equal to 0')
        self._interval: Final[float] = interval
        self._clean_interval: Final[float] = (
            clean_interval if clean_interval > 0 else interval)
        self._events: Final[Dict[Hashable, asyncio.Event]] = {}
        self._ts: Final[Dict[Hashable, float]] = {}
        self._clean_event: Final = asyncio.Event()
        self._clean_task: Optional[asyncio.Task] = None

    async def reset(self) -> None:
        if self._clean_task is not None:
            self._clean_task.cancel()
            with suppress(asyncio.CancelledError):
                await self._clean_task
            self._clean_task = None
        self._events.clear()
        self._ts.clear()
        self._clean_event.clear()

    @asynccontextmanager
    async def acquire(
        self, key: Hashable = None
    ) -> AsyncGenerator[None, None]:
        loop = asyncio.get_running_loop()
        if self._clean_task is None:
            self._clean_task = loop.create_task(self._clean())
        while True:
            if key not in self._events:
                self._events[key] = asyncio.Event()
                self._ts[key] = -float('inf')
                break
            else:
                await self._events[key].wait()
                if key in self._events and self._events[key].is_set():
                    self._events[key].clear()
                    break
        delay = self._interval - loop.time() + self._ts[key]
        if delay > 0:
            await asyncio.sleep(delay)
        self._ts[key] = loop.time()
        try:
            yield
        finally:
            self._events[key].set()
            self._clean_event.set()

    async def _clean(self) -> None:
        loop = asyncio.get_running_loop()
        while True:
            if len(self._events) == 0:
                await self._clean_event.wait()
                self._clean_event.clear()
            for key, event in self._events.copy().items():
                age = loop.time() - self._ts[key]
                if event.is_set() and age >= self._clean_interval:
                    del self._events[key]
            for key in self._ts.copy().keys():
                if key not in self._events:
                    del self._ts[key]
            await asyncio.sleep(self._clean_interval)
