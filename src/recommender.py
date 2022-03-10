import json

import spotipy
from configparser import ConfigParser
from spotipy.oauth2 import SpotifyClientCredentials


class Recommender:
    def __init__(self, config: ConfigParser):
        self._config = config
        self._client_id = self._config.get('RECOMMENDER', 'client_id')
        self._client_secret = self._config.get('RECOMMENDER', 'client_secret')
        # Authorize via spotify and save the auth token in _sp
        auth_manager = SpotifyClientCredentials(client_id=self._client_id, client_secret=self._client_secret)
        self._sp = spotipy.Spotify(auth_manager=auth_manager)

    def find_playlist_id(self, auth_token: str, location: str):
        # Search for the term "location" and return the first playlist
        result = self._sp.search(location, type="playlist", limit=1)
        # Find the ID of the playlist (nested dict)
        return result["playlists"]["items"][0]["id"]

    def get_songs(self, auth_token: str, playlist_id: str):
        # Retrieve tracks from the given playlist, only return the track id
        result = self._sp.playlist_items(playlist_id, limit=10)

        # Find the track ID of every track in the dict, and add them to an array
        tracks = []
        for item in result["items"]:
            artist_list = []
            for artist in item["track"]["artists"]:
                artist_list.append(artist["name"])
            artists = ", ".join(artist_list)

            images = item["track"]["album"]["images"]
            images_sorted = sorted(images, key=lambda d: d["width"])
            image_url = images_sorted[0]["url"]
            
            track_dict = {
                "id": item["track"]["id"],
                "name": item["track"]["name"],
                "artist": artists,
                "image": image_url
            }
            #name, artist, cover art, id
            tracks.append(track_dict)

        parsed_result = {
            "result": {
                "id": "placeholder",
                "location_type": "placeholder",
                "tracks": tracks
            },
            "is_successful": "placeholder",
            "error_no": 0
        }

        return json.dumps(parsed_result, indent=4)
