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
        raise Exception("Deprecated")

    def org_attributes_as_vec(self):
        raise Exception("Deprecated")

    def as_np_vec(self):
        raise Exception("Deprecated")