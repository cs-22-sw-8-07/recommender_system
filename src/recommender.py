from spotify_requests import SpotifyRequests
from service_response import service_response_error_json
from service_response import Errors
from service_response import service_response_playlist_json
from vector_space_model import VectorSpaceModel


class Recommender:
    def __init__(self, spotify_requests: SpotifyRequests):
        self._sr = spotify_requests
        self._feature_vecs = {"forest": [0.3314020000000001, 0.3492549999999999, -18.01141, 0.07096000000000002, 0.7168996, 0.5430275521000002, 0.3319970000000001, 0.1, 110.28479999999998]}
        self._vsm = VectorSpaceModel()
        self._vsm.load_csv(r"C:\Users\Jeppe\Downloads\archive\tracks.csv")

    def get_playlist(self, location: str):
        error_no = 0

        try:
            error_no = Errors.CouldNotFindClosestTracks
            tracks = self._vsm.closest_tracks(self._feature_vecs[location])

            error_no = Errors.CouldNotFormatSongListToJson
            return self.get_playlist_json(tracks, location)
        except:
            return service_response_error_json(error_no.value)

    def get_playlist_json(self, tracks, location):
        # Find the track ID of every track in the dict, and add them to an array
        tracks_formatted = []
        for track in tracks:
            # Add all artists to one string, comma seperated
            #artist_list = []
            #for artist in track.artists:
            #    artist_list.append(artist)
            #artists = ", ".join(artist_list)

            # Find the image URL of the smallest available cover art image
            #images = item["track"]["album"]["images"]
            #images_sorted = sorted(images, key=lambda d: d["width"])
            #image_url = images_sorted[0]["url"]

            # Format the track with the necessary info
            track_dict = {
                "id": track.id,
                "name": track.name,
                "artist": track.artists,
                # "image": image_url
                "image": "none"
            }
            tracks_formatted.append(track_dict)

        return service_response_playlist_json(tracks_formatted, location)
