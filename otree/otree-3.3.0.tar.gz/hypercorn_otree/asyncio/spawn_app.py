import asyncio
from typing import Awaitable, Callable

from .task_group import TaskGroup
from ..config import Config
from ..typing import ASGIFramework
from ..utils import invoke_asgi


async def _handle(
    app: ASGIFramework, config: Config, scope: dict, receive: Callable, send: Callable
) -> None:
    try:
        await invoke_asgi(app, scope, receive, send)
    except asyncio.CancelledError:
        raise
    except Exception:
        await config.log.exception("Error in ASGI Framework")
    finally:
        await send(None)


async def spawn_app(
    task_group: TaskGroup,
    app: ASGIFramework,
    config: Config,
    scope: dict,
    send: Callable[[dict], Awaitable[None]],
) -> Callable[[dict], Awaitable[None]]:
    app_queue: asyncio.Queue = asyncio.Queue(config.max_app_queue_size)
    task_group.spawn(_handle(app, config, scope, app_queue.get, send))
    return app_queue.put
