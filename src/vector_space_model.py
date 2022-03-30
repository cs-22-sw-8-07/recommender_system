import ast
import pandas
import numpy as np
from pandas import DataFrame


class Track:
    line_no: int
    id: str
    name: str
    popularity: float
    duration_ms: int
    explicit: bool
    artists: []
    id_artists: []
    release_date: str
    danceability: float
    energy: float
    key: float
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    vec: []

    def normalize_vec(self, min_vec, max_vec):
        for i in range(0, len(self.vec)):
            if max_vec[i] - min_vec[i] == 0:
                continue

            self.vec[i] = (self.vec[i] - min_vec[i])/(max_vec[i] - min_vec[i])


    def org_attributes_as_vec(self):
        return [self.danceability,
                self.energy,
                self.loudness,
                self.speechiness,
                self.acousticness,
                self.instrumentalness,
                self.liveness,
                self.valence,
                self.tempo]

    def as_np_vec(self):
        return np.array(self.vec)


class VectorSpaceModel:
    def __init__(self):
        self._data: DataFrame = None
        self._tracks = []
        self._min_vec = []
        self._max_vec = []

    def load_csv(self, csv_path: str):
        self._data = pandas.read_csv(csv_path)
        self._tracks = []
        line = 1
        values_in_vec = 0

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
            track.danceability = v[8]
            track.energy = v[9]
            track.key = v[10]
            track.loudness = v[11]
            track.mode = v[12]
            track.speechiness = v[13]
            track.acousticness = v[14]
            track.instrumentalness = v[15]
            track.liveness = v[16]
            track.valence = v[17]
            track.tempo = v[18]
            track.time_signature = v[19]
            track.vec = track.org_attributes_as_vec()
            self._tracks.append(track)
            values_in_vec = len(track.vec)

        # Normalize values in vectors
        self._min_vec = [9999.0 for _ in range(0, values_in_vec)]
        self._max_vec = [-9999.0 for _ in range(0, values_in_vec)]
        for i in range(0, len(self._tracks)):
            for j in range(0, len(self._tracks[i].vec)):
                if self._min_vec[j] > self._tracks[i].vec[j]:
                    self._min_vec[j] = self._tracks[i].vec[j]
                if self._max_vec[j] < self._tracks[i].vec[j]:
                    self._max_vec[j] = self._tracks[i].vec[j]

        for t in self._tracks:
            t.normalize_vec(self._min_vec, self._max_vec)

    def _compare_euclidian(self, track_1: Track, track_2: Track) -> float:
        return np.linalg.norm(track_1.as_np_vec() - track_2.as_np_vec())

    def closest_tracks(self, feature_vec: [], amount: int = 10):
        track = Track()
        track.vec = feature_vec
        track.normalize_vec(self._min_vec, self._max_vec)
        sorted_tracks = sorted(self._tracks, key=lambda t: self._compare_euclidian(t, track))
        return sorted_tracks[0:amount]


