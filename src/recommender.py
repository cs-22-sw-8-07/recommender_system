from src.spotify_requests import SpotifyRequests
from src.service_response import service_response_error_json
from src.service_response import Errors
from src.service_response import service_response_playlist_json


class Recommender:
    def __init__(self, spotify_requests: SpotifyRequests):
        self._sr = spotify_requests

    def get_playlist(self, location: str):
        error_no = 0

        try:
            error_no = Errors.CouldNotFindPlaylists
            playlists = self._sr.find_playlists(location, 1)

            error_no = Errors.CouldNotFindSongsFromPlaylist
            playlist_id = playlists["playlists"]["items"][0]["id"]
            song_list = self._sr.find_songs(playlist_id, 10)

            error_no = Errors.CouldNotFormatSongListToJson
            return self.get_playlist_json(song_list, location)
        except:
            return service_response_error_json(error_no.value)

    def get_playlist_json(self, song_list, location):
        # Find the track ID of every track in the dict, and add them to an array
        tracks = []
        for item in song_list["items"]:
            # Add all artists to one string, comma seperated
            artist_list = []
            for artist in item["track"]["artists"]:
                artist_list.append(artist["name"])
            artists = ", ".join(artist_list)

            # Find the image URL of the smallest available cover art image
            images = item["track"]["album"]["images"]
            images_sorted = sorted(images, key=lambda d: d["width"])
            image_url = images_sorted[0]["url"]

            # Format the track with the necessary info
            track_dict = {
                "id": item["track"]["id"],
                "name": item["track"]["name"],
                "artist": artists,
                "image": image_url
            }
            tracks.append(track_dict)

        return service_response_playlist_json(tracks, location)
