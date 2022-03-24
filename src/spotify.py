import spotipy
from configparser import ConfigParser
from spotipy.oauth2 import SpotifyClientCredentials
from tests.mock_data import MockData


class Spotify:
    def __init__(self, config: ConfigParser, auth_token):
        self._use_mock_data = config.getboolean('SPOTIFY', 'use_mock_data')
        self._sp = spotipy.Spotify(auth=auth_token)

    def find_playlists(self, location: str, limit: int):
        # Search for the term "location" and return the number of playlist according to the limit
        return self._sp.search(location, type="playlist", limit=limit)

    def find_songs(self, playlist_id: str, limit: int):
        if self._use_mock_data:
            return MockData().mock_find_songs

        # Retrieve tracks from the given playlist, only return the track id
        return self._sp.playlist_items(playlist_id, limit=limit)
