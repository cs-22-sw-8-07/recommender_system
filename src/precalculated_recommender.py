import os
import pandas
from configparser import ConfigParser
from pandas.errors import EmptyDataError
from quack_location_type import QuackLocationType
from recommender import Recommender
from service_response import Errors, service_response_error_json


class PrecalcTrack:
    id = ""
    name = ""
    artists = []
    image = "none"


class PrecalculatedRecommender(Recommender):
    def __init__(self, config: ConfigParser, recommender_type: str):
        super().__init__()
        self._config = config
        self._page_size = self._config.getint("PRECALCULATED_RECOMMENDER", "page_size")
        self._recommender_type = recommender_type
        self.test_mode = False

    def get_playlist(self, location: QuackLocationType, previous_offsets: list):
        error_no = 0

        try:
            error_no = Errors.CouldNotReadPrecalculatedDataSet
            base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
            recommender_tracks_folder = self._get_folder_name(self._recommender_type)
            tracks_file = self._get_csv_file_name(location)
            if not self.test_mode:
                resources_folder = "resources"
            else:
                resources_folder = os.path.join("tests", "test_resources")
            path = os.path.join(base_folder, resources_folder, recommender_tracks_folder, tracks_file)

            if len(previous_offsets) == 0:
                target_page = 0
            else:
                target_page = max(previous_offsets) + 1
            offset = target_page * self._page_size
            values = []

            while True:
                try:
                    data = pandas.read_csv(path, header=None, skiprows=offset, nrows=self._page_size)
                    values = data.values
                    break
                except EmptyDataError:
                    if offset == 0:
                        values = []
                        break
                    offset = 0
                    target_page = 0
                    continue

            if len(values) == 0:
                error_no = Errors.NoTracksInTargetLocation
                raise Exception

            error_no = Errors.CouldNotTransformCSVIntoCorrectFormat
            formatted_tracks = []
            for row in values:
                track = PrecalcTrack()
                track.id = row[0]
                track.name = row[1]
                track.artists = row[2].split(";")
                if len(row) > 3:
                    track.image = row[3]
                formatted_tracks.append(track)

            error_no = Errors.CouldNotFormatSongListToJson
            return self._get_playlist_json(formatted_tracks, location, target_page)
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
