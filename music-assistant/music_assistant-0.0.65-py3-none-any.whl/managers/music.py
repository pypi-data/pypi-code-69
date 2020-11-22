"""MusicManager: Orchestrates all data from music providers and sync to internal database."""

import asyncio
import logging
from typing import List

from music_assistant.helpers.cache import async_cached
from music_assistant.helpers.compare import (
    compare_album,
    compare_strings,
    compare_track,
)
from music_assistant.helpers.encryption import async_encrypt_string
from music_assistant.helpers.musicbrainz import MusicBrainz
from music_assistant.helpers.util import unique_item_ids
from music_assistant.helpers.web import api_route
from music_assistant.models.media_types import (
    Album,
    Artist,
    FullAlbum,
    FullTrack,
    MediaItem,
    MediaType,
    Playlist,
    Radio,
    SearchResult,
    Track,
)
from music_assistant.models.provider import MusicProvider, ProviderType
from music_assistant.models.streamdetails import ContentType, StreamDetails, StreamType

LOGGER = logging.getLogger("music_manager")


class MusicManager:
    """Several helpers around the musicproviders."""

    def __init__(self, mass):
        """Initialize class."""
        self.mass = mass
        self.cache = mass.cache
        self.musicbrainz = MusicBrainz(mass)

    async def async_setup(self):
        """Async initialize of module."""

    @property
    def providers(self) -> List[MusicProvider]:
        """Return all providers of type musicprovider."""
        return self.mass.get_providers(ProviderType.MUSIC_PROVIDER)

    ################ GET MediaItem(s) by id and provider #################

    @api_route("items/:media_type/:provider_id/:item_id")
    async def async_get_item(
        self, item_id: str, provider_id: str, media_type: MediaType
    ):
        """Get single music item by id and media type."""
        if media_type == MediaType.Artist:
            return await self.async_get_artist(item_id, provider_id)
        if media_type == MediaType.Album:
            return await self.async_get_album(item_id, provider_id)
        if media_type == MediaType.Track:
            return await self.async_get_track(item_id, provider_id)
        if media_type == MediaType.Playlist:
            return await self.async_get_playlist(item_id, provider_id)
        if media_type == MediaType.Radio:
            return await self.async_get_radio(item_id, provider_id)
        return None

    @api_route("artists/:provider_id/:item_id")
    async def async_get_artist(
        self, item_id: str, provider_id: str, refresh=False
    ) -> Artist:
        """Return artist details for the given provider artist id."""
        if provider_id == "database" and not refresh:
            return await self.mass.database.async_get_artist(item_id)
        db_item = await self.mass.database.async_get_artist_by_prov_id(
            provider_id, item_id
        )
        if db_item and refresh:
            provider_id, item_id = await self.__get_provider_id(db_item)
        elif db_item:
            return db_item
        artist = await self.__async_get_provider_artist(item_id, provider_id)
        # fetching an artist is slow because of musicbrainz and metadata lookup
        # so we return the provider object
        self.mass.add_job(self.async_add_artist(artist))
        return artist

    async def __async_get_provider_artist(
        self, item_id: str, provider_id: str
    ) -> Artist:
        """Return artist details for the given provider artist id."""
        provider = self.mass.get_provider(provider_id)
        if not provider or not provider.available:
            raise Exception("Provider %s is not available!" % provider_id)
        cache_key = f"{provider_id}.get_artist.{item_id}"
        artist = await async_cached(
            self.cache, cache_key, provider.async_get_artist, item_id
        )
        if not artist:
            raise Exception(
                "Artist %s not found on provider %s" % (item_id, provider_id)
            )
        return artist

    @api_route("albums/:provider_id/:item_id")
    async def async_get_album(
        self, item_id: str, provider_id: str, refresh=False
    ) -> Album:
        """Return album details for the given provider album id."""
        if provider_id == "database" and not refresh:
            return await self.mass.database.async_get_album(item_id)
        db_item = await self.mass.database.async_get_album_by_prov_id(
            provider_id, item_id
        )
        if db_item and refresh:
            provider_id, item_id = await self.__get_provider_id(db_item)
        elif db_item:
            return db_item
        album = await self.__async_get_provider_album(item_id, provider_id)
        return await self.async_add_album(album)

    async def __async_get_provider_album(self, item_id: str, provider_id: str) -> Album:
        """Return album details for the given provider album id."""
        provider = self.mass.get_provider(provider_id)
        if not provider or not provider.available:
            raise Exception("Provider %s is not available!" % provider_id)
        cache_key = f"{provider_id}.get_album.{item_id}"
        album = await async_cached(
            self.cache, cache_key, provider.async_get_album, item_id
        )
        if not album:
            raise Exception(
                "Album %s not found on provider %s" % (item_id, provider_id)
            )
        return album

    @api_route("tracks/:provider_id/:item_id")
    async def async_get_track(
        self,
        item_id: str,
        provider_id: str,
        track_details: Track = None,
        album_details: Album = None,
        refresh: bool = False,
    ) -> Track:
        """Return track details for the given provider track id."""
        if provider_id == "database" and not refresh:
            return await self.mass.database.async_get_track(item_id)
        db_item = await self.mass.database.async_get_track_by_prov_id(
            provider_id, item_id
        )
        if db_item and refresh:
            # in some cases (e.g. at playback time or requesting full track info)
            # it's useful to have the track refreshed from the provider instead of
            # the database cache to make sure that the track is available and perhaps
            # another or a higher quality version is available.
            provider_id, item_id = await self.__get_provider_id(db_item)
        elif db_item:
            return db_item
        if not track_details:
            track_details = await self.__async_get_provider_track(item_id, provider_id)
        if album_details:
            track_details.album = album_details
        return await self.async_add_track(track_details)

    async def __async_get_provider_track(self, item_id: str, provider_id: str) -> Album:
        """Return track details for the given provider track id."""
        provider = self.mass.get_provider(provider_id)
        if not provider or not provider.available:
            raise Exception("Provider %s is not available!" % provider_id)
        cache_key = f"{provider_id}.get_track.{item_id}"
        track = await async_cached(
            self.cache, cache_key, provider.async_get_track, item_id
        )
        if not track:
            raise Exception(
                "Track %s not found on provider %s" % (item_id, provider_id)
            )
        return track

    @api_route("playlists/:provider_id/:item_id")
    async def async_get_playlist(self, item_id: str, provider_id: str) -> Playlist:
        """Return playlist details for the given provider playlist id."""
        assert item_id and provider_id
        db_item = await self.mass.database.async_get_playlist_by_prov_id(
            provider_id, item_id
        )
        if not db_item:
            # item not yet in local database so fetch and store details
            provider = self.mass.get_provider(provider_id)
            if not provider.available:
                return None
            item_details = await provider.async_get_playlist(item_id)
            db_item = await self.mass.database.async_add_playlist(item_details)
        return db_item

    @api_route("radios/:provider_id/:item_id")
    async def async_get_radio(self, item_id: str, provider_id: str) -> Radio:
        """Return radio details for the given provider playlist id."""
        assert item_id and provider_id
        db_item = await self.mass.database.async_get_radio_by_prov_id(
            provider_id, item_id
        )
        if not db_item:
            # item not yet in local database so fetch and store details
            provider = self.mass.get_provider(provider_id)
            if not provider.available:
                return None
            item_details = await provider.async_get_radio(item_id)
            db_item = await self.mass.database.async_add_radio(item_details)
        return db_item

    @api_route("albums/:provider_id/:item_id/tracks")
    async def async_get_album_tracks(
        self, item_id: str, provider_id: str
    ) -> List[Track]:
        """Return album tracks for the given provider album id."""
        assert item_id and provider_id
        album = await self.async_get_album(item_id, provider_id)
        if album.provider == "database":
            # album tracks are not stored in db, we always fetch them (cached) from the provider.
            provider_id = album.provider_ids[0].provider
            item_id = album.provider_ids[0].item_id
        provider = self.mass.get_provider(provider_id)
        cache_key = f"{provider_id}.album_tracks.{item_id}"
        all_prov_tracks = await async_cached(
            self.cache, cache_key, provider.async_get_album_tracks, item_id
        )
        # retrieve list of db items
        db_tracks = await self.mass.database.async_get_tracks_from_provider_ids(
            [x.provider for x in album.provider_ids],
            [x.item_id for x in all_prov_tracks],
        )
        # combine provider tracks with db tracks
        return [
            await self.__process_item(
                item,
                db_tracks,
                album=album,
                disc_number=item.disc_number,
                track_number=item.track_number,
            )
            for item in all_prov_tracks
        ]

    @api_route("albums/:provider_id/:item_id/versions")
    async def async_get_album_versions(
        self, item_id: str, provider_id: str
    ) -> List[Album]:
        """Return all versions of an album we can find on all providers."""
        album = await self.async_get_album(item_id, provider_id)
        provider_ids = [
            item.id for item in self.mass.get_providers(ProviderType.MUSIC_PROVIDER)
        ]
        search_query = f"{album.artist.name} - {album.name}"
        result = []
        for prov_id in provider_ids:
            provider_result = await self.async_search_provider(
                search_query, prov_id, [MediaType.Album], 25
            )
            for item in provider_result.albums:
                if compare_strings(item.artist.name, album.artist.name):
                    result.append(item)
        return result

    @api_route("tracks/:provider_id/:item_id/versions")
    async def async_get_track_versions(
        self, item_id: str, provider_id: str
    ) -> List[Track]:
        """Return all versions of a track we can find on all providers."""
        track = await self.async_get_track(item_id, provider_id)
        provider_ids = [
            item.id for item in self.mass.get_providers(ProviderType.MUSIC_PROVIDER)
        ]
        search_query = f"{track.artists[0].name} - {track.name}"
        result = []
        for prov_id in provider_ids:
            provider_result = await self.async_search_provider(
                search_query, prov_id, [MediaType.Track], 25
            )
            for item in provider_result.tracks:
                if not compare_strings(item.name, track.name):
                    continue
                for artist in item.artists:
                    # artist must match
                    if compare_strings(artist.name, track.artists[0].name):
                        result.append(item)
                        break
        return result

    @api_route("playlists/:provider_id/:item_id/tracks")
    async def async_get_playlist_tracks(
        self, item_id: str, provider_id: str
    ) -> List[Track]:
        """Return playlist tracks for the given provider playlist id."""
        assert item_id and provider_id
        if provider_id == "database":
            # playlist tracks are not stored in db, we always fetch them (cached) from the provider.
            playlist = await self.mass.database.async_get_playlist(item_id)
            provider_id = playlist.provider_ids[0].provider
            item_id = playlist.provider_ids[0].item_id
            provider = self.mass.get_provider(provider_id)
        else:
            provider = self.mass.get_provider(provider_id)
            playlist = await provider.async_get_playlist(item_id)
        cache_checksum = playlist.checksum
        cache_key = f"{provider_id}.playlist_tracks.{item_id}"
        playlist_tracks = await async_cached(
            self.cache,
            cache_key,
            provider.async_get_playlist_tracks,
            item_id,
            checksum=cache_checksum,
        )
        db_tracks = await self.mass.database.async_get_tracks_from_provider_ids(
            provider_id, [x.item_id for x in playlist_tracks]
        )
        # combine provider tracks with db tracks
        return [
            await self.__process_item(item, db_tracks, index)
            for index, item in enumerate(playlist_tracks)
        ]

    async def __process_item(
        self,
        item,
        db_items,
        index=None,
        album=None,
        disc_number=None,
        track_number=None,
    ):
        """Return combined result of provider item and db result."""
        for db_item in db_items:
            if item.item_id in [x.item_id for x in db_item.provider_ids]:
                item = db_item
                break
        if index is not None and not item.position:
            item.position = index
        if album is not None:
            item.album = album
        if disc_number is not None:
            item.disc_number = disc_number
        if track_number is not None:
            item.track_number = track_number
        # make sure artists are unique
        if hasattr(item, "artists"):
            item.artists = unique_item_ids(item.artists)
        return item

    @api_route("artists/:provider_id/:item_id/tracks")
    async def async_get_artist_toptracks(
        self, item_id: str, provider_id: str
    ) -> List[Track]:
        """Return top tracks for an artist."""
        artist = await self.async_get_artist(item_id, provider_id)
        # get results from all providers
        all_prov_tracks = [
            track
            for prov_tracks in await asyncio.gather(
                *[
                    self.__async_get_provider_artist_toptracks(
                        item.item_id, item.provider
                    )
                    for item in artist.provider_ids
                ]
            )
            for track in prov_tracks
        ]
        # retrieve list of db items
        db_tracks = await self.mass.database.async_get_tracks_from_provider_ids(
            [x.provider for x in artist.provider_ids],
            [x.item_id for x in all_prov_tracks],
        )
        # combine provider tracks with db tracks and filter duplicate itemid's
        return unique_item_ids(
            [await self.__process_item(item, db_tracks) for item in all_prov_tracks]
        )

    async def __async_get_provider_artist_toptracks(
        self, item_id: str, provider_id: str
    ) -> List[Track]:
        """Return top tracks for an artist on given provider."""
        provider = self.mass.get_provider(provider_id)
        if not provider or not provider.available:
            LOGGER.error("Provider %s is not available", provider_id)
            return []
        cache_key = f"{provider_id}.artist_toptracks.{item_id}"
        return await async_cached(
            self.cache,
            cache_key,
            provider.async_get_artist_toptracks,
            item_id,
        )

    @api_route("artists/:provider_id/:item_id/albums")
    async def async_get_artist_albums(
        self, item_id: str, provider_id: str
    ) -> List[Album]:
        """Return (all) albums for an artist."""
        artist = await self.async_get_artist(item_id, provider_id)
        # get results from all providers
        all_prov_albums = [
            album
            for prov_albums in await asyncio.gather(
                *[
                    self.__async_get_provider_artist_albums(item.item_id, item.provider)
                    for item in artist.provider_ids
                ]
            )
            for album in prov_albums
        ]
        # retrieve list of db items
        db_tracks = await self.mass.database.async_get_albums_from_provider_ids(
            [x.provider for x in artist.provider_ids],
            [x.item_id for x in all_prov_albums],
        )
        # combine provider tracks with db tracks and filter duplicate itemid's
        return unique_item_ids(
            [await self.__process_item(item, db_tracks) for item in all_prov_albums]
        )

    async def __async_get_provider_artist_albums(
        self, item_id: str, provider_id: str
    ) -> List[Album]:
        """Return albums for an artist on given provider."""
        provider = self.mass.get_provider(provider_id)
        if not provider or not provider.available:
            LOGGER.error("Provider %s is not available", provider_id)
            return []
        cache_key = f"{provider_id}.artist_albums.{item_id}"
        return await async_cached(
            self.cache,
            cache_key,
            provider.async_get_artist_albums,
            item_id,
        )

    @api_route("search/:provider_id")
    async def async_search_provider(
        self,
        search_query: str,
        provider_id: str,
        media_types: List[MediaType],
        limit: int = 10,
    ) -> SearchResult:
        """
        Perform search on given provider.

            :param search_query: Search query
            :param provider_id: provider_id of the provider to perform the search on.
            :param media_types: A list of media_types to include. All types if None.
            :param limit: number of items to return in the search (per type).
        """
        if provider_id == "database":
            # get results from database
            return await self.mass.database.async_search(search_query, media_types)
        provider = self.mass.get_provider(provider_id)
        cache_key = f"{provider_id}.search.{search_query}.{media_types}.{limit}"
        return await async_cached(
            self.cache,
            cache_key,
            provider.async_search,
            search_query,
            media_types,
            limit,
        )

    @api_route("search")
    async def async_global_search(
        self, search_query, media_types: List[MediaType], limit: int = 10
    ) -> SearchResult:
        """
        Perform global search for media items on all providers.

            :param search_query: Search query.
            :param media_types: A list of media_types to include.
            :param limit: number of items to return in the search (per type).
        """
        result = SearchResult([], [], [], [], [])
        # include results from all music providers
        provider_ids = ["database"] + [
            item.id for item in self.mass.get_providers(ProviderType.MUSIC_PROVIDER)
        ]
        for provider_id in provider_ids:
            provider_result = await self.async_search_provider(
                search_query, provider_id, media_types, limit
            )
            result.artists += provider_result.artists
            result.albums += provider_result.albums
            result.tracks += provider_result.tracks
            result.playlists += provider_result.playlists
            result.radios += provider_result.radios
            # TODO: sort by name and filter out duplicates ?
        return result

    async def async_get_stream_details(
        self, media_item: MediaItem, player_id: str = ""
    ) -> StreamDetails:
        """
        Get streamdetails for the given media_item.

        This is called just-in-time when a player/queue wants a MediaItem to be played.
        Do not try to request streamdetails in advance as this is expiring data.
            param media_item: The MediaItem (track/radio) for which to request the streamdetails for.
            param player_id: Optionally provide the player_id which will play this stream.
        """
        if media_item.provider == "uri":
            # special type: a plain uri was added to the queue
            streamdetails = StreamDetails(
                type=StreamType.URL,
                provider="uri",
                item_id=media_item.item_id,
                path=media_item.item_id,
                content_type=ContentType(media_item.item_id.split(".")[-1]),
                sample_rate=44100,
                bit_depth=16,
            )
        else:
            # always request the full db track as there might be other qualities available
            # except for radio
            if media_item.media_type == MediaType.Radio:
                full_track = media_item
            else:
                full_track = await self.async_get_track(
                    media_item.item_id, media_item.provider, refresh=True
                )
            # sort by quality and check track availability
            for prov_media in sorted(
                full_track.provider_ids, key=lambda x: x.quality, reverse=True
            ):
                if not prov_media.available:
                    continue
                # get streamdetails from provider
                music_prov = self.mass.get_provider(prov_media.provider)
                if not music_prov or not music_prov.available:
                    continue  # provider temporary unavailable ?

                streamdetails: StreamDetails = (
                    await music_prov.async_get_stream_details(prov_media.item_id)
                )
                if streamdetails:
                    try:
                        streamdetails.content_type = ContentType(
                            streamdetails.content_type
                        )
                    except KeyError:
                        LOGGER.warning("Invalid content type!")
                    else:
                        break

        if streamdetails:
            # set player_id on the streamdetails so we know what players stream
            streamdetails.player_id = player_id
            # store the path encrypted as we do not want it to be visible in the api
            streamdetails.path = await async_encrypt_string(streamdetails.path)
            # set streamdetails as attribute on the media_item
            # this way the app knows what content is playing
            media_item.streamdetails = streamdetails
            return streamdetails
        return None

    ################ ADD MediaItem(s) to database helpers ################

    async def async_add_artist(self, artist: Artist) -> int:
        """Add artist to local db and return the database item."""
        if not artist.musicbrainz_id:
            artist.musicbrainz_id = await self.__async_get_artist_musicbrainz_id(artist)
        # grab additional metadata
        artist.metadata = await self.mass.metadata.async_get_artist_metadata(
            artist.musicbrainz_id, artist.metadata
        )
        db_item = await self.mass.database.async_add_artist(artist)
        # also fetch same artist on all providers
        self.mass.add_background_task(self.async_match_artist(db_item))
        self.mass.signal_event("artist added", db_item)
        return db_item

    async def async_add_album(self, album: Album) -> int:
        """Add album to local db and return the database item."""
        # make sure we have an artist
        assert album.artist
        db_item = await self.mass.database.async_add_album(album)
        # also fetch same album on all providers
        self.mass.add_background_task(self.async_match_album(db_item))
        self.mass.signal_event("album added", db_item)
        return db_item

    async def async_add_track(self, track: Track) -> int:
        """Add track to local db and return the new database id."""
        # make sure we have artists
        assert track.artists
        # make sure we have an album
        assert track.album or track.albums
        db_item = await self.mass.database.async_add_track(track)
        # also fetch same track on all providers (will also get other quality versions)
        self.mass.add_background_task(self.async_match_track(db_item))
        return db_item

    async def __async_get_artist_musicbrainz_id(self, artist: Artist):
        """Fetch musicbrainz id by performing search using the artist name, albums and tracks."""
        # try with album first
        for lookup_album in await self.__async_get_provider_artist_albums(
            artist.item_id, artist.provider
        ):
            if not lookup_album:
                continue
            musicbrainz_id = await self.musicbrainz.async_get_mb_artist_id(
                artist.name,
                albumname=lookup_album.name,
                album_upc=lookup_album.upc,
            )
            if musicbrainz_id:
                return musicbrainz_id
        # fallback to track
        for lookup_track in await self.__async_get_provider_artist_toptracks(
            artist.item_id, artist.provider
        ):
            if not lookup_track:
                continue
            musicbrainz_id = await self.musicbrainz.async_get_mb_artist_id(
                artist.name,
                trackname=lookup_track.name,
                track_isrc=lookup_track.isrc,
            )
            if musicbrainz_id:
                return musicbrainz_id
        # lookup failed, use the shitty workaround to use the name as id.
        LOGGER.warning("Unable to get musicbrainz ID for artist %s !", artist.name)
        return artist.name

    async def async_match_artist(self, db_artist: Artist):
        """
        Try to find matching artists on all providers for the provided (database) item_id.

        This is used to link objects of different providers together.
        """
        assert (
            db_artist.provider == "database"
        ), "Matching only supported for database items!"
        cur_providers = [item.provider for item in db_artist.provider_ids]
        for provider in self.mass.get_providers(ProviderType.MUSIC_PROVIDER):
            if provider.id in cur_providers:
                continue
            if Artist not in provider.supported_mediatypes:
                continue
            if not await self.__async_match_prov_artist(db_artist, provider):
                LOGGER.debug(
                    "Could not find match for Artist %s on provider %s",
                    db_artist.name,
                    provider.name,
                )

    async def __async_match_prov_artist(
        self, db_artist: Artist, provider: MusicProvider
    ):
        """Try to find matching artists on given provider for the provided (database) artist."""
        LOGGER.debug(
            "Trying to match artist %s on provider %s", db_artist.name, provider.name
        )
        # try to get a match with some reference albums of this artist
        for ref_album in await self.async_get_artist_albums(
            db_artist.item_id, db_artist.provider
        ):
            searchstr = "%s - %s" % (db_artist.name, ref_album.name)
            search_result = await self.async_search_provider(
                searchstr, provider.id, [MediaType.Album], limit=10
            )
            for search_result_item in search_result.albums:
                if compare_album(search_result_item, ref_album):
                    # 100% album match, we can simply update the db with the provider id
                    await self.mass.database.async_update_artist(
                        db_artist.item_id, search_result_item.artist
                    )
                    return True

        # try to get a match with some reference tracks of this artist
        for ref_track in await self.async_get_artist_toptracks(
            db_artist.item_id, db_artist.provider
        ):
            searchstr = "%s - %s" % (db_artist.name, ref_track.name)
            search_results = await self.async_search_provider(
                searchstr, provider.id, [MediaType.Track], limit=10
            )
            for search_result_item in search_results.tracks:
                if compare_track(search_result_item, ref_track):
                    # get matching artist from track
                    for search_item_artist in search_result_item.artists:
                        if compare_strings(db_artist.name, search_item_artist.name):
                            # 100% match, we can simply update the db with additional provider ids
                            await self.mass.database.async_update_artist(
                                db_artist.item_id, search_item_artist
                            )
                            return True
        return False

    async def async_match_album(self, db_album: Album):
        """
        Try to find matching album on all providers for the provided (database) album_id.

        This is used to link objects of different providers/qualities together.
        """
        assert (
            db_album.provider == "database"
        ), "Matching only supported for database items!"
        if not isinstance(db_album, FullAlbum):
            # matching only works if we have a full album object
            db_album = await self.mass.database.async_get_album(db_album.item_id)

        async def find_prov_match(provider):
            LOGGER.debug(
                "Trying to match album %s on provider %s", db_album.name, provider.name
            )
            match_found = False
            searchstr = "%s - %s" % (db_album.artist.name, db_album.name)
            if db_album.version:
                searchstr += " " + db_album.version
            search_result = await self.async_search_provider(
                searchstr, provider.id, [MediaType.Album], limit=5
            )
            for search_result_item in search_result.albums:
                if not search_result_item.available:
                    continue
                if compare_album(search_result_item, db_album):
                    # 100% match, we can simply update the db with additional provider ids
                    await self.mass.database.async_update_album(
                        db_album.item_id, search_result_item
                    )
                    match_found = True
            # no match found
            if not match_found:
                LOGGER.debug(
                    "Could not find match for Album %s on provider %s",
                    db_album.name,
                    provider.name,
                )

        # try to find match on all providers
        providers = self.mass.get_providers(ProviderType.MUSIC_PROVIDER)
        for provider in providers:
            if Album in provider.supported_mediatypes:
                await find_prov_match(provider)

    async def async_match_track(self, db_track: Track):
        """
        Try to find matching track on all providers for the provided (database) track_id.

        This is used to link objects of different providers/qualities together.
        """
        assert (
            db_track.provider == "database"
        ), "Matching only supported for database items!"
        if not isinstance(db_track, FullTrack):
            # matching only works if we have a full track object
            db_track = await self.mass.database.async_get_track(db_track.item_id)
        for provider in self.mass.get_providers(ProviderType.MUSIC_PROVIDER):
            if Track not in provider.supported_mediatypes:
                continue
            LOGGER.debug(
                "Trying to match track %s on provider %s", db_track.name, provider.name
            )
            match_found = False
            for db_track_artist in db_track.artists:
                if match_found:
                    break
                searchstr = "%s - %s" % (db_track_artist.name, db_track.name)
                if db_track.version:
                    searchstr += " " + db_track.version
                search_result = await self.async_search_provider(
                    searchstr, provider.id, [MediaType.Track], limit=10
                )
                for search_result_item in search_result.tracks:
                    if not search_result_item.available:
                        continue
                    if compare_track(search_result_item, db_track):
                        # 100% match, we can simply update the db with additional provider ids
                        match_found = True
                        await self.mass.database.async_update_track(
                            db_track.item_id, search_result_item
                        )

            if not match_found:
                LOGGER.debug(
                    "Could not find match for Track %s on provider %s",
                    db_track.name,
                    provider.name,
                )

    async def __get_provider_id(self, media_item: MediaItem) -> tuple:
        """Return provider and item id."""
        if media_item.provider == "database":
            media_item = await self.mass.database.async_get_item_by_prov_id(
                "database", media_item.item_id, media_item.media_type
            )
            for prov in media_item.provider_ids:
                if prov.available and self.mass.get_provider(prov.provider):
                    provider = self.mass.get_provider(prov.provider)
                    if provider and provider.available:
                        return (prov.provider, prov.item_id)
        else:
            provider = self.mass.get_provider(media_item.provider)
            if provider and provider.available:
                return (media_item.provider, media_item.item_id)
        return None, None
