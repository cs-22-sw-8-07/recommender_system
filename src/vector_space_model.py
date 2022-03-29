import pandas
import numpy as np
from pandas import DataFrame, Series


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

    def as_vec(self):
        return np.array((self.danceability,
                         self.energy,
                         self.loudness,
                         self.speechiness,
                         self.acousticness,
                         self.instrumentalness,
                         self.liveness,
                         self.valence,
                         self.tempo))


class VectorSpaceModel:
    def __init__(self):
        self._data: DataFrame = None
        self._tracks: Track = []

    def load_csv(self, csv_path: str):
        self._data = pandas.read_csv(csv_path)
        self._tracks = []
        line = 0
        for f in self._data.values:
            track = Track()
            track.line_no = line
            track.id = f[0]
            track.name = f[1]
            track.popularity = f[2]
            track.duration_ms = f[3]
            track.explicit = f[4]
            track.artists = f[5]
            track.id_artists = f[6]
            track.release_date = f[7]
            track.danceability = f[8]
            track.energy = f[9]
            track.key = f[10]
            track.loudness = f[11]
            track.mode = f[12]
            track.speechiness = f[13]
            track.acousticness = f[14]
            track.instrumentalness = f[15]
            track.liveness = f[16]
            track.valence = f[17]
            track.tempo = f[18]
            track.time_signature = f[19]
            self._tracks.append(track)
            line += 1

    def _compare_euclidian(self, track_1: Track, track_2: Track) -> float:
        return np.linalg.norm(track_1.as_vec() - track_2.as_vec())

    def closest_tracks(self, track: Track, amount: int = 10):
        sorted_tracks = sorted(self._tracks, key=lambda t: self._compare_euclidian(t, track))
        return sorted_tracks[0:amount]


