import pandas


class TrackData:
    def __init__(self):
        self._dict = {}
        self._min_vec = []
        self._max_vec = []

    def __getitem__(self, item):
        return self._dict[item]

    def load_csv(self, path: str):
        self._dict = {}
        data = pandas.read_csv(path)
        for v in data.values:
            if v[1] not in self._dict.keys():
                self._dict[v[1]] = []

            new_vec = [v[5], v[6], v[8]]
            new_vec.extend(v[10:16])
            self._dict[v[1]].append(new_vec)

        self._normalize()

    def keys(self):
        return list(self._dict.keys())

    def size_of_vecs(self) -> int:
        return len(list(self._dict.values())[0][0])

    def _normalize(self):
        size_of_vecs = self.size_of_vecs()
        track_values = self._values()

        self._min_vec = [9999.0 for _ in range(0, size_of_vecs)]
        self._max_vec = [-9999.0 for _ in range(0, size_of_vecs)]
        for i in range(0, len(track_values)):
            for j in range(0, size_of_vecs):
                if self._min_vec[j] > track_values[i][j]:
                    self._min_vec[j] = track_values[i][j]
                if self._max_vec[j] < track_values[i][j]:
                    self._max_vec[j] = track_values[i][j]

        for key in self._dict.keys():
            for i in range(0, len(self._dict[key])):
                for j in range(0, len(self._dict[key][i])):
                    if self._max_vec[j] == self._min_vec[j]:
                        continue

                    self._dict[key][i][j] = (self._dict[key][i][j] - self._min_vec[j])/(self._max_vec[j] - self._min_vec[j])

    def _values(self):
        # Flattens a structure [[1, 2], [3, 4]] -> [1, 2, 3, 4]
        return [val for values in self._dict.values() for val in values]
