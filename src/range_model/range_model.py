import ast
import os
import pandas
from configparser import ConfigParser
from track import Track
from quack_location_type import QuackLocationType
from track_data import TrackData


class RangeModel:
    def __init__(self, config: ConfigParser):
        self._slice_pct = config.getfloat('RANGE_MODEL', 'slice_percentage')
        self._no_of_range_attributes = config.getint('RANGE_MODEL', 'no_of_range_attributes')
        self._track_data = TrackData()
        self._bottom_range = {}
        self._top_range = {}
        self._range_attribute_priority = {}
        self._tracks = []
        self._data = None
        self._tracks = []

        base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..")
        path = os.path.join(base_folder, "resources", "CompleteIndividualTrackData.csv")
        self._track_data.load_csv(path)
        self._create_ranges()

    def _create_ranges(self):
        self._bottom_range = {}
        self._top_range = {}
        self._range_attribute_priority = {}
        difference = {}
        size_of_vecs = self._track_data.size_of_vecs()

        for key in self._track_data.keys():
            self._bottom_range[key] = [0 for _ in range(0, size_of_vecs)]
            self._top_range[key] = [1 for _ in range(0, size_of_vecs)]
            difference[key] = [0 for _ in range(0, size_of_vecs)]
            for i in range(0, size_of_vecs):
                sorted_vars = sorted(self._track_data[key], key=lambda v: v[i])
                self._bottom_range[key][i] = sorted_vars[int(self._track_data.tracks_in_key(key) * self._slice_pct)][i]
                self._top_range[key][i] = sorted_vars[int(self._track_data.tracks_in_key(key) * 1 - self._slice_pct)][i]
                difference[key][i] = self._top_range[key][i] - self._bottom_range[key][i]

        for key in self._track_data.keys():
            self._range_attribute_priority[key] = [0 for _ in range(0, size_of_vecs)]
            sorted_diff = sorted(difference[key])
            self._range_attribute_priority[key][difference[key].index(sorted_diff[0])] = 2
            for i in range(1, self._no_of_range_attributes):
                self._range_attribute_priority[key][difference[key].index(sorted_diff[i])] = 1

    def load_track_csv(self, csv_path: str):
        self._data = pandas.read_csv(csv_path)
        self._tracks = []
        line = 1

        for v in self._data.values:
            line += 1
            track = Track()
            track.line_no = line
            track.id = v[0]
            track.name = v[1]
            track.popularity = v[2]
            track.duration_ms = v[3]
            track.explicit = v[4]
            track.artists = ast.literal_eval(v[5])
            track.id_artists = ast.literal_eval(v[6])
            track.release_date = v[7]
            track.key = v[10]
            track.mode = v[12]
            track.time_signature = v[19]
            track.attribute_vec = [v[8], v[9], v[11]]
            track.attribute_vec.extend(v[13:19])
            self._track_data.normalize_vec(track.attribute_vec)
            self._tracks.append(track)

    def _range_filter(self, vec, bottom, top):
        for i in range(0, len(bottom)):
            if vec[i] < bottom[i] or vec[i] > top[i]:
                return False
        return True

    def get_tracks(self, location_type: QuackLocationType):
        key = location_type.name

        filter_bottom = [-9999.0 for _ in range(0, self._track_data.size_of_vecs())]
        filter_top = [9999.0 for _ in range(0, self._track_data.size_of_vecs())]

        for i in range(0, len(self._track_data.keys())):
            if not self._range_attribute_priority[key][i]:
                continue

            filter_bottom[i] = self._bottom_range[key][i]
            filter_top[i] = self._top_range[key][i]

        filtered = list(filter(lambda track: self._range_filter(track.attribute_vec, filter_bottom, filter_top), self._tracks))
        sort = list(sorted(filtered, key=lambda track: track.popularity, reverse=True))[0:10]
        print("Bla")



