import os
import pandas
from pandas.errors import EmptyDataError

from quack_location_type import QuackLocationType
from recommender import Recommender
from service_response import Errors, service_response_error_json


class PrecalcTrack:
    id = ""
    name = ""
    artists = []
    image = ""


class PrecalculatedRecommender(Recommender):
    def __init__(self, recommender_type: str):
        self._recommender_type = recommender_type
        super().__init__()

    def get_playlist(self, location: QuackLocationType, amount: int = 10, offset: int = 0):
        error_no = 0

        try:
            error_no = Errors.CouldNotReadPrecalculatedDataSet
            base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
            recommender_tracks_folder = self._get_folder_name(self._recommender_type)
            tracks_file = self._get_csv_file_name(location)
            path = os.path.join(base_folder, "resources", recommender_tracks_folder, tracks_file)

            try:
                data = pandas.read_csv(path, header=None, skiprows=offset, nrows=amount)
                values = data.values
            except EmptyDataError:
                values = []

            error_no = Errors.CouldNotTransformCSVIntoCorrectFormat
            formatted_tracks = []
            for row in values:
                track = PrecalcTrack()
                track.id = row[0]
                track.name = row[1]
                track.artists = row[2].split(";")
                track.image = row[3]
                formatted_tracks.append(track)

            error_no = Errors.CouldNotFormatSongListToJson
            return self._get_playlist_json(formatted_tracks, location)
        except:
            return service_response_error_json(error_no.value)

    def _get_folder_name(self, recommender_type: str):
        match recommender_type:
            case "distance" | "range":
                return recommender_type + "_recommender_tracks"
            case _:
                raise Exception("Not a recommender type")

    def _get_csv_file_name(self, location: QuackLocationType):
        return location.name + "_tracks.csv"
