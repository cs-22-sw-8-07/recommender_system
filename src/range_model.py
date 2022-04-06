import os
from quack_location_type import QuackLocationType
from track_data import TrackData


class RangeModel:
    def __init__(self):
        self._track_data = TrackData()
        self._min_dict = {}
        self._max_dict = {}

        base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        path = os.path.join(base_folder, "resources", "CompleteIndividualTrackData.csv")
        self._track_data.load_csv(path)

        self._create_ranges()

    def _create_ranges(self):
        size_of_vecs = self._track_data.size_of_vecs()

        for key in self._track_data.keys():
            self._min_dict[key] = [9999.0 for _ in range(0, size_of_vecs)]
            self._max_dict[key] = [-9999.0 for _ in range(0, size_of_vecs)]

            for i in range(0, len(self._track_data[key])):
                for j in range(0, len(self._track_data[key][i])):
                    if self._min_dict[key][j] > self._track_data[key][i][j]:
                        self._min_dict[key][j] = self._track_data[key][i][j]
                    if self._max_dict[key][j] < self._track_data[key][i][j]:
                        self._max_dict[key][j] = self._track_data[key][i][j]

    def get_tracks(self, location_type: QuackLocationType):
        pass


