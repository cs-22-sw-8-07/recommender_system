import os
from configparser import ConfigParser
from quack_location_type import QuackLocationType
from track_data import TrackData


class RangeModel:
    def __init__(self, config: ConfigParser):
        self._slice_percentage = config.getfloat('RANGE_MODEL', 'slice_percentage')
        self._no_of_range_attributes = config.getint('RANGE_MODEL', 'no_of_range_attributes')
        self._track_data = TrackData()
        self._min_dict = {}
        self._max_dict = {}

        base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        path = os.path.join(base_folder, "resources", "CompleteIndividualTrackData.csv")
        self._track_data.load_csv(path)

        self._create_ranges()

    def _create_ranges(self):
        size_of_vecs = self._track_data.size_of_vecs()

        track_data_agg = self._track_data.copy_dict()
        bottom_range_dict = {}
        top_range_dict = {}
        difference = {}
        range_attribute = {}

        for key in self._track_data.keys():
            bottom_range_dict[key] = [0 for _ in range(0, size_of_vecs)]
            top_range_dict[key] = [1 for _ in range(0, size_of_vecs)]
            difference[key] = [0 for _ in range(0, size_of_vecs)]
            for i in range(0, size_of_vecs):
                sorted_vars = sorted(track_data_agg[key], key=lambda v: v[i])
                bottom_range_dict[key][i] = sorted_vars[int(self._track_data.tracks_in_key(key)*self._slice_percentage)][i]
                top_range_dict[key][i] = sorted_vars[int(self._track_data.tracks_in_key(key)*1-self._slice_percentage)][i]
                difference[key][i] = top_range_dict[key][i] - bottom_range_dict[key][i]

        for key in self._track_data.keys():
            range_attribute[key] = [False for _ in range(0, size_of_vecs)]
            sorted_diff = sorted(difference[key])
            for i in range(0, self._no_of_range_attributes):
                range_attribute[key][difference[key].index(sorted_diff[i])] = True

    def get_tracks(self, location_type: QuackLocationType):
        pass


