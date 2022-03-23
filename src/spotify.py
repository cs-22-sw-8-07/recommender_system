import spotipy
from configparser import ConfigParser
from spotipy.oauth2 import SpotifyClientCredentials


class Spotify:
    def __init__(self, auth_token):
        self._sp = spotipy.Spotify(auth=auth_token)

    def find_playlists(self, location: str, limit: int):
        # Search for the term "location" and return the number of playlist according to the limit
        return self._sp.search(location, type="playlist", limit=limit)

    def find_songs(self, playlist_id: str, limit: int):
        # Retrieve tracks from the given playlist, only return the track id
        return self._sp.playlist_items(playlist_id, limit=limit)
