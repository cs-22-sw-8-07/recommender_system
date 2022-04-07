from distance_model.feature_vector import FeatureVector
from service_response import service_response_error_json
from service_response import Errors
from service_response import service_response_playlist_json
from distance_model.vector_space_model import VectorSpaceModel


class Recommender:
    def __init__(self, feature_vec: FeatureVector, vsm: VectorSpaceModel):
        self._feature_vec = feature_vec
        self._vsm = vsm

    def get_playlist(self, location: str):
        error_no = 0

        try:
            error_no = Errors.CouldNotFindClosestTracks
            tracks = self._vsm.closest_tracks(self._feature_vec[location])

            error_no = Errors.CouldNotFormatSongListToJson
            return self.get_playlist_json(tracks, location)
        except:
            return service_response_error_json(error_no.value)

    def get_playlist_json(self, tracks, location):
        # Find the track ID of every track in the dict, and add them to an array
        tracks_formatted = []
        for track in tracks:
            # Add all artists to one string, comma seperated
            artist_list = []
            for artist in track.artists:
                artist_list.append(artist)
            artists = ", ".join(artist_list)

            # Format the track with the necessary info
            track_dict = {
                "id": track.id,
                "name": track.name,
                "artist": artists,
                "image": "none"
            }
            tracks_formatted.append(track_dict)

        return service_response_playlist_json(tracks_formatted, location)
