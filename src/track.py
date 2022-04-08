import numpy as np


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
    key: float
    mode: int
    time_signature: int
    attribute_vec: []

    def normalize_vec(self, min_vec, max_vec):
        for i in range(0, len(self.attribute_vec)):
            if max_vec[i] - min_vec[i] == 0:
                continue

            self.attribute_vec[i] = (self.attribute_vec[i] - min_vec[i])/(max_vec[i] - min_vec[i])

    def as_np_vec(self):
        return np.array(self.attribute_vec)
