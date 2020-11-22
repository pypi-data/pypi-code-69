from typing import Union

import aiohttp

from ...config import Config
from .melon import resolve as melon_resolve
from .spotify import resolve as spotify_resolve


async def resolve(
    query: str, connector: aiohttp.TCPConnector = None
) -> Union[str, list]:
    if "melon" in Config.ENABLED_EXT_RESOLVER:
        query = await melon_resolve(query, connector)
    if "spotify" in Config.ENABLED_EXT_RESOLVER:
        query = await spotify_resolve(query)

    return query
