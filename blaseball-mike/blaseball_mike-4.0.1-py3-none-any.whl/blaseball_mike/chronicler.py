"""Client for chronicler APIs

API Reference (out of date): https://astrid.stoplight.io/docs/sibr/reference/Chronicler.v1.yaml
"""
import requests_cache
import requests
from datetime import datetime

BASE_URL = 'https://api.sibr.dev/chronicler/v1'
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

cached_session = requests_cache.CachedSession(backend="memory")

def prepare_id(id_):
    """if id_ is string uuid, return as is, if list, format as comma separated list."""
    if isinstance(id_, list):
        return ','.join(id_)
    elif isinstance(id_, str):
        return id_
    else:
        raise ValueError(f'Incorrect ID type: {type(id_)}')


def paged_get(url, params, session=None):
    data = []
    while(True):
        if not session:
            out = requests.get(url, params=params).json()
        else:
            out = session.get(url, params=params).json()
        d = out.get("data", [])
        page = out.get("nextPage")
        
        data.extend(d)
        if page is None or len(d) == 0 or params.get("count", 1000) >= len(d):
            break
        params["page"] = page

    return data


def get_games(season=None, day=None, team_ids=None, pitcher_ids=None, weather=None, started=None, finished=None, outcomes=None, order=None, count=None):
    params = {}
    if season is not None:
        params["season"] = season - 1
    if day:
        params["day"] = day - 1
    if order:
        params["order"] = order
    if count:
        params["count"] = count
    if team_ids:
        params["team"] = prepare_id(team_ids)
    if pitcher_ids:
        params["pitcher"] = prepare_id(pitcher_ids)
    if started:
        params["started"] = started
    if finished:
        params["finished"] = finished
    if outcomes:
        params["outcomes"] = outcomes
    if weather:
        params["weather"] = weather

    data = paged_get(f'{BASE_URL}/games', params=params, session=cached_session)
    return {p['gameId']: p for p in data}


def get_player_updates(ids=None, before=None, after=None, order=None, count=None):
    if isinstance(before, datetime):
        before = before.strftime(TIMESTAMP_FORMAT)
    if isinstance(after, datetime):
        after = after.strftime(TIMESTAMP_FORMAT)

    params = {}
    if before:
        params["before"] = before
    if after:
        params["after"] = after
    if order:
        params["order"] = order
    if count:
        params["count"] = count
    if ids:
        params["player"] = prepare_id(ids)

    data = paged_get(f'{BASE_URL}/players/updates', params=params, session=cached_session)
    return {p['playerId']: p for p in data}


def get_player_history(id_, before=None, after=None, order=None, count=None):
    """
    Returns list of dicts of a single player's history
    """
    if isinstance(before, datetime):
        before = before.strftime(TIMESTAMP_FORMAT)
    if isinstance(after, datetime):
        after = after.strftime(TIMESTAMP_FORMAT)
    params = {
        'player': id_,
    }
    if before:
        params["before"] = before
    if after:
        params["after"] = after
    if order:
        params["order"] = order
    if count:
        params["count"] = count
    data = paged_get(f'{BASE_URL}/players/updates', params=params, session=cached_session)
    return [d for d in data]


def get_team_updates(ids=None, before=None, after=None, order=None, count=None):
    if isinstance(before, datetime):
        before = before.strftime(TIMESTAMP_FORMAT)
    if isinstance(after, datetime):
        after = after.strftime(TIMESTAMP_FORMAT)

    params = {}
    if before:
        params["before"] = before
    if after:
        params["after"] = after
    if order:
        params["order"] = order
    if count:
        params["count"] = count
    if ids:
        params["team"] = prepare_id(ids)

    data = paged_get(f'{BASE_URL}/teams/updates', params=params, session=cached_session)
    return {p['teamId']: p for p in data}


def get_tribute_updates(before=None, after=None, order=None, count=None):
    if isinstance(before, datetime):
        before = before.strftime(TIMESTAMP_FORMAT)
    if isinstance(after, datetime):
        after = after.strftime(TIMESTAMP_FORMAT)

    params = {}
    if before:
        params["before"] = before
    if after:
        params["after"] = after
    if order:
        params["order"] = order
    if count:
        params["count"] = count

    data = paged_get(f'{BASE_URL}/tributes/hourly', params=params, session=cached_session)
    return {p['timestamp']: p for p in data}
