from quack_location_type import QuackLocationType
from recommender import Recommender
from service_response import Errors, service_response_error_json
from range_model.range_model import RangeModel


class RangeRecommender(Recommender):
    def __init__(self, range_model: RangeModel):
        super().__init__()
        self._range_model = range_model

    def get_playlist(self, location: QuackLocationType, amount: int, offset: int):
        error_no = 0

        try:
            error_no = Errors.CouldNotFindTracksFromRangeRecommender
            tracks = self._range_model.get_tracks(location, amount, offset)

            error_no = Errors.CouldNotFormatSongListToJson
            return self._get_playlist_json(tracks, location)
        except:
            return service_response_error_json(error_no.value)
