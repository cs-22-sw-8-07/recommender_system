import json
import os
from unittest import TestCase

from src.recommender import Recommender
from tests.mock_data import MockData_SpotifyRequests


class TestRecommender(TestCase):
    test_mock_data = None
    recommender = None

    def setUp(self):
        spotify = MockData_SpotifyRequests()
        self.recommender = Recommender(spotify)

    def test_get_playlist(self):
        expected_result_str = """{"result": {"location_type": "forest", "tracks": [{"id": "1Pcr11BvLJJldjWqpdDp2l", "name": "All We Have Is Now", "artist": "Ross Copperman", "image": "https://i.scdn.co/image/ab67616d000048515fde2391a4d930feb4f976eb"}, {"id": "0aufeXojH6SvCzlEJPAlbg", "name": "Motives", "artist": "Davis John Patton", "image": "https://i.scdn.co/image/ab67616d00004851507cb18a80cf2b85305ee1e8"}, {"id": "03cDw9iq5KedboH2bU6G1p", "name": "Forever Ago", "artist": "Woodlock", "image": "https://i.scdn.co/image/ab67616d0000485195aec74758da0acf4e956907"}, {"id": "1uliNs1keVwYclj74JX44R", "name": "Decimal", "artist": "Novo Amor", "image": "https://i.scdn.co/image/ab67616d00004851402890963386e03ceeabdf35"}, {"id": "5GhWXAiU0dIROxSgWWTV3H", "name": "Evermore", "artist": "Hollow Coves", "image": "https://i.scdn.co/image/ab67616d000048511cb13205eaf944e3f18c8fce"}, {"id": "19jTCAxeVnkwKnWHSsdg0i", "name": "Lucky for You", "artist": "Novo Amor, Gia Margaret", "image": "https://i.scdn.co/image/ab67616d000048517fefbd580ac79842fe6bac14"}, {"id": "28sWYevC75ZrUMJ0tD4zWM", "name": "These Memories", "artist": "Hollow Coves", "image": "https://i.scdn.co/image/ab67616d00004851e771a39481e5b482af5ffe0c"}, {"id": "4fGgmcD5Ke4I4ZfJ1hZeiW", "name": "Never Stop", "artist": "Tyler Brown Williams", "image": "https://i.scdn.co/image/ab67616d0000485128a379899af02a2dbc95fdfe"}, {"id": "07oIgOa6p1MZZqD8XelNq2", "name": "Marigolds", "artist": "Boundary Run", "image": "https://i.scdn.co/image/ab67616d00004851351146f381bca84f32ec6c31"}, {"id": "1npKCqB7DQ8bAM1DlWp5a9", "name": "Haven Lea", "artist": "Lists", "image": "https://i.scdn.co/image/ab67616d000048517cb13f53e4b6bd6d28cd9bd3"}]}, "is_successful": 1, "error_no": 0}"""
        expected_result = json.loads(expected_result_str)

        result_str = self.recommender.get_playlist("forest")
        result = json.loads(result_str)
        result["result"].pop("id")

        self.assertEqual(result, expected_result)

    def test_get_playlist_json(self):
        pass