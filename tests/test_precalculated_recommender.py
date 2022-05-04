import json
from unittest import TestCase
from precalculated_recommender import PrecalculatedRecommender
from config import load_config
from quack_location_type import QuackLocationType


class TestPrecalculatedRecommender(TestCase):
    def setUp(self):
        self.config = load_config("test_config.cnf")
        self.recommender = PrecalculatedRecommender(self.config, "range")
        self.recommender.test_mode = True

    def test_get_playlist__forest_no_offset(self):
        expected_result_str = """{"result": {"offset": 0, "location_type": 4, "tracks": [{"id": "4tKpJR6k6rANU8dEE74jqW", "name": "Forest Track 01", "artist": "Artist 01", "image": "https://i.scdn.co/image/ab67616d00004851d4fcda9a09f59fa1394e7a43"}, {"id": "2ffDtMWivVnr4Z3kNBda8y", "name": "Forest Track 02", "artist": "Artist 02", "image": "https://i.scdn.co/image/ab67616d00004851ae259c2d7863335b5fb5040b"}, {"id": "4KEDJUs8n2Fk0EY7a6DHd1", "name": "Forest Track 03", "artist": "Artist 03", "image": "https://i.scdn.co/image/ab67616d000048517ab1b51f3a37b29b782b3e94"}, {"id": "1BVF4c964LEMZTH5FTgF7Y", "name": "Forest Track 04", "artist": "Artist 04", "image": "https://i.scdn.co/image/ab67616d00004851195de9e8d2f7eec205025726"}, {"id": "0HUmIBR5vEcL7E3cbjo3Hh", "name": "Forest Track 05", "artist": "Artist 05", "image": "https://i.scdn.co/image/ab67616d00004851801dcfaa97db998cf6e9766e"}, {"id": "449Q8hJDTgx41QX5gKlLEb", "name": "Forest Track 06", "artist": "Artist 06", "image": "https://i.scdn.co/image/ab67616d00004851c6797d2be95f29e697ddf664"}, {"id": "1C5HpiqUgOY7v5audtXeXa", "name": "Forest Track 07", "artist": "Artist 07", "image": "https://i.scdn.co/image/ab67616d00004851564f4fd1da117b9d43e4784b"}, {"id": "05k4IbZ6GqPpAw0Gi64hWN", "name": "Forest Track 08", "artist": "Artist 08", "image": "https://i.scdn.co/image/ab67616d00004851d269c5893083edc669c215e2"}, {"id": "3jkcGBQGiMQbh8r1am6UWE", "name": "Forest Track 09", "artist": "Artist 09", "image": "https://i.scdn.co/image/ab67616d00004851734d441bde333305c42a0796"}, {"id": "3IFEbjQqyHgc7saidYSdUI", "name": "Forest Track 10", "artist": "Artist 10", "image": "https://i.scdn.co/image/ab67616d0000485161cfadfbc0632bb33463c040"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender.get_playlist(QuackLocationType.forest, [])
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)

    def test_get_playlist__forest_offset_1(self):
        expected_result_str = """{"result": {"offset": 1, "location_type": 4, "tracks": [{"id": "3BrTgcdCjGx7PlxJn2qFlv", "name": "Forest Track 11", "artist": "Artist 11", "image": "https://i.scdn.co/image/ab67616d00004851071137676cb6ec4e19dc1bab"}, {"id": "4cmTpKba9EuR6FFNjsNKT2", "name": "Forest Track 12", "artist": "Artist 12", "image": "https://i.scdn.co/image/ab67616d0000485154f314d4c988be8a3a45bd87"}, {"id": "34HAgdOLarlciwtmcTooA3", "name": "Forest Track 13", "artist": "Artist 13", "image": "https://i.scdn.co/image/ab67616d00004851841598b4f6fc6eb5944dbb66"}, {"id": "6dAS2i3A0pTv4KNZ2JLTQw", "name": "Forest Track 14", "artist": "Artist 14", "image": "https://i.scdn.co/image/ab67616d00004851004fc8e7a2ba853f540d65ee"}, {"id": "3eqsh8q9i9KECm6p93fT4h", "name": "Forest Track 15", "artist": "Artist 15, Additional Artist 1, Additional Artist 2", "image": "https://i.scdn.co/image/ab67616d0000485180a906606cc4c427b5a58b5c"}, {"id": "2LdMNVdeAgU83z3phU5UO9", "name": "Forest Track 16", "artist": "Artist 16", "image": "https://i.scdn.co/image/ab67616d0000485145313620d5436e37fbf17fd2"}, {"id": "4wN3gnjYsVHcPM9Do8EkGT", "name": "Forest Track 17", "artist": "Artist 17", "image": "https://i.scdn.co/image/ab67616d00004851622281583f5aeb3e23b4b026"}, {"id": "6Dt6vUL6iKTNWi5OC7kv5Y", "name": "Forest Track 18", "artist": "Artist 18", "image": "https://i.scdn.co/image/ab67616d00004851cfb2250b180c328d6a5940e5"}, {"id": "6WkNAujl93Ho8EebRDmZZy", "name": "Forest Track 19", "artist": "Artist 19", "image": "https://i.scdn.co/image/ab67616d000048519a2fcc14dae33d3870ab736d"}, {"id": "1i115TFyD2RHBmlcJpHAxI", "name": "Forest Track 20", "artist": "Artist 20", "image": "https://i.scdn.co/image/ab67616d00004851353e37aaddee2838a229c5fc"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender.get_playlist(QuackLocationType.forest, [0])
        result_json = json.loads(result_str)

        print(result_str)
        self.assertEqual(expected_result_json, result_json)

    def test_get_playlist__forest_offset_2(self):
        expected_result_str = """{"result": {"offset": 2, "location_type": 4, "tracks": [{"id": "4tKpJR6k6rANU8dEE74jqW", "name": "Forest Track 21", "artist": "Artist 01", "image": "https://i.scdn.co/image/ab67616d00004851d4fcda9a09f59fa1394e7a43"}, {"id": "2ffDtMWivVnr4Z3kNBda8y", "name": "Forest Track 22", "artist": "Artist 02", "image": "https://i.scdn.co/image/ab67616d00004851ae259c2d7863335b5fb5040b"}, {"id": "4KEDJUs8n2Fk0EY7a6DHd1", "name": "Forest Track 23", "artist": "Artist 03", "image": "https://i.scdn.co/image/ab67616d000048517ab1b51f3a37b29b782b3e94"}, {"id": "1BVF4c964LEMZTH5FTgF7Y", "name": "Forest Track 24", "artist": "Artist 04", "image": "https://i.scdn.co/image/ab67616d00004851195de9e8d2f7eec205025726"}, {"id": "0HUmIBR5vEcL7E3cbjo3Hh", "name": "Forest Track 25", "artist": "Artist 05", "image": "https://i.scdn.co/image/ab67616d00004851801dcfaa97db998cf6e9766e"}, {"id": "449Q8hJDTgx41QX5gKlLEb", "name": "Forest Track 26", "artist": "Artist 06", "image": "https://i.scdn.co/image/ab67616d00004851c6797d2be95f29e697ddf664"}, {"id": "1C5HpiqUgOY7v5audtXeXa", "name": "Forest Track 27", "artist": "Artist 07", "image": "https://i.scdn.co/image/ab67616d00004851564f4fd1da117b9d43e4784b"}, {"id": "05k4IbZ6GqPpAw0Gi64hWN", "name": "Forest Track 28", "artist": "Artist 08", "image": "https://i.scdn.co/image/ab67616d00004851d269c5893083edc669c215e2"}, {"id": "3jkcGBQGiMQbh8r1am6UWE", "name": "Forest Track 29", "artist": "Artist 09", "image": "https://i.scdn.co/image/ab67616d00004851734d441bde333305c42a0796"}, {"id": "3IFEbjQqyHgc7saidYSdUI", "name": "Forest Track 30", "artist": "Artist 10", "image": "https://i.scdn.co/image/ab67616d0000485161cfadfbc0632bb33463c040"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender.get_playlist(QuackLocationType.forest, [0, 1])
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)

    def test_get_playlist__forest_offset_out_of_range(self):
        expected_result_str = """{"result": {"offset": 0, "location_type": 4, "tracks": [{"id": "4tKpJR6k6rANU8dEE74jqW", "name": "Forest Track 01", "artist": "Artist 01", "image": "https://i.scdn.co/image/ab67616d00004851d4fcda9a09f59fa1394e7a43"}, {"id": "2ffDtMWivVnr4Z3kNBda8y", "name": "Forest Track 02", "artist": "Artist 02", "image": "https://i.scdn.co/image/ab67616d00004851ae259c2d7863335b5fb5040b"}, {"id": "4KEDJUs8n2Fk0EY7a6DHd1", "name": "Forest Track 03", "artist": "Artist 03", "image": "https://i.scdn.co/image/ab67616d000048517ab1b51f3a37b29b782b3e94"}, {"id": "1BVF4c964LEMZTH5FTgF7Y", "name": "Forest Track 04", "artist": "Artist 04", "image": "https://i.scdn.co/image/ab67616d00004851195de9e8d2f7eec205025726"}, {"id": "0HUmIBR5vEcL7E3cbjo3Hh", "name": "Forest Track 05", "artist": "Artist 05", "image": "https://i.scdn.co/image/ab67616d00004851801dcfaa97db998cf6e9766e"}, {"id": "449Q8hJDTgx41QX5gKlLEb", "name": "Forest Track 06", "artist": "Artist 06", "image": "https://i.scdn.co/image/ab67616d00004851c6797d2be95f29e697ddf664"}, {"id": "1C5HpiqUgOY7v5audtXeXa", "name": "Forest Track 07", "artist": "Artist 07", "image": "https://i.scdn.co/image/ab67616d00004851564f4fd1da117b9d43e4784b"}, {"id": "05k4IbZ6GqPpAw0Gi64hWN", "name": "Forest Track 08", "artist": "Artist 08", "image": "https://i.scdn.co/image/ab67616d00004851d269c5893083edc669c215e2"}, {"id": "3jkcGBQGiMQbh8r1am6UWE", "name": "Forest Track 09", "artist": "Artist 09", "image": "https://i.scdn.co/image/ab67616d00004851734d441bde333305c42a0796"}, {"id": "3IFEbjQqyHgc7saidYSdUI", "name": "Forest Track 10", "artist": "Artist 10", "image": "https://i.scdn.co/image/ab67616d0000485161cfadfbc0632bb33463c040"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender.get_playlist(QuackLocationType.forest, [0, 1, 2, 3])
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)

    def test_get_playlist__beach_no_data(self):
        expected_result_str = """{"is_successful": 0,"error_no": 128,"error_msg": "NoTracksInTargetLocation"}"""
        expected_result_json = json.loads(expected_result_str)

        result_str = self.recommender.get_playlist(QuackLocationType.beach, [])
        result_json = json.loads(result_str)

        self.assertEqual(expected_result_json, result_json)

    def test_get_folder_name__distance(self):
        expected_result = "distance_recommender_tracks"

        result = self.recommender._get_folder_name("distance")

        self.assertEqual(expected_result, result)

    def test_get_folder_name__range(self):
        expected_result = "range_recommender_tracks"

        result = self.recommender._get_folder_name("range")

        self.assertEqual(expected_result, result)

    def test_get_folder_name__unknown(self):
        try:
            self.recommender._get_folder_name("unknown")
        except:
            return

        self.fail()

    def test_get_csv_file_name__forest(self):
        expected_result = "forest_tracks.csv"

        result = self.recommender._get_csv_file_name(QuackLocationType.forest)

        self.assertEqual(expected_result, result)

    def test_get_csv_file_name__beach(self):
        expected_result = "beach_tracks.csv"

        result = self.recommender._get_csv_file_name(QuackLocationType.beach)

        self.assertEqual(expected_result, result)
