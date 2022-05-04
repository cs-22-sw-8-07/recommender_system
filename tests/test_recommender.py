import json
from unittest import TestCase
from config import load_config
from quack_location_type import QuackLocationType
from recommender import Recommender


class TestTrack:
    def __init__(self, id, name, artists, image):
        self.id = id
        self.name = name
        self.artists = artists
        self.image = image


class TestRecommender(TestCase):
    def setUp(self):
        self.config = load_config("test_config.cnf")
        self.recommender = Recommender()
        self.tracks = [
            TestTrack("id1", "name1", ["artist1"], "image1"),
            TestTrack("id2", "name2", ["artist2", "additional artist1", "additional artist2"], "image2"),
            TestTrack("id3", "name3", ["artist3"], "image3"),
            TestTrack("id4", "name4", ["artist4", "additional artist3"], "image4"),
            TestTrack("id5", "name5", ["artist5"], "image5"),
        ]

    def test_get_playlist(self):
        try:
            self.recommender.get_playlist(QuackLocationType.forest, [])
        except:
            return

        self.fail()

    def test_get_playlist_json__forest_offset0(self):
        expected_result_str = """{"result": {"offset": 0, "location_type": 4, "tracks": [{"id": "id1", "name": "name1", "artist": "artist1", "image": "image1"}, {"id": "id2", "name": "name2", "artist": "artist2, additional artist1, additional artist2", "image": "image2"}, {"id": "id3", "name": "name3", "artist": "artist3", "image": "image3"}, {"id": "id4", "name": "name4", "artist": "artist4, additional artist3", "image": "image4"}, {"id": "id5", "name": "name5", "artist": "artist5", "image": "image5"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender._get_playlist_json(self.tracks, QuackLocationType.forest, 0)
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)

    def test_get_playlist_json__beach_offset0(self):
        expected_result_str = """{"result": {"offset": 0, "location_type": 5, "tracks": [{"id": "id1", "name": "name1", "artist": "artist1", "image": "image1"}, {"id": "id2", "name": "name2", "artist": "artist2, additional artist1, additional artist2", "image": "image2"}, {"id": "id3", "name": "name3", "artist": "artist3", "image": "image3"}, {"id": "id4", "name": "name4", "artist": "artist4, additional artist3", "image": "image4"}, {"id": "id5", "name": "name5", "artist": "artist5", "image": "image5"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender._get_playlist_json(self.tracks, QuackLocationType.beach, 0)
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)

    def test_get_playlist_json__beach_offset1(self):
        expected_result_str = """{"result": {"offset": 1, "location_type": 5, "tracks": [{"id": "id1", "name": "name1", "artist": "artist1", "image": "image1"}, {"id": "id2", "name": "name2", "artist": "artist2, additional artist1, additional artist2", "image": "image2"}, {"id": "id3", "name": "name3", "artist": "artist3", "image": "image3"}, {"id": "id4", "name": "name4", "artist": "artist4, additional artist3", "image": "image4"}, {"id": "id5", "name": "name5", "artist": "artist5", "image": "image5"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender._get_playlist_json(self.tracks, QuackLocationType.beach, 1)
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)
