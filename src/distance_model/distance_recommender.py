from distance_model.feature_vector import FeatureVector
from distance_model.vector_space_model import VectorSpaceModel
from quack_location_type import QuackLocationType
from recommender import Recommender
from service_response import Errors, service_response_error_json


class DistanceRecommender(Recommender):
    def __init__(self, feature_vec: FeatureVector, vsm: VectorSpaceModel):
        super().__init__()
        self._feature_vec = feature_vec
        self._vsm = vsm

    def get_playlist(self, location: QuackLocationType, amount: int, offset: int):
        key = location.name
        error_no = 0

        try:
            error_no = Errors.CouldNotFindClosestTracks
            tracks = self._vsm.closest_tracks(self._feature_vec[key], amount)

            error_no = Errors.CouldNotFormatSongListToJson
            return self._get_playlist_json(tracks, location)
        except:
            return service_response_error_json(error_no.value)
