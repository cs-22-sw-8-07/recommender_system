import os
from unittest import TestCase

from src.recommender import Recommender
from tests.mock_data import TestMockData


class TestRecommender(TestCase):
    test_mock_data = None
    recommender = None

    def setUp(self):
        self.test_mock_data = TestMockData()
        self.recommender = Recommender(self.test_mock_data.config)

    def test_get_playlist(self):
        self.fail()

    def test_get_playlist_json(self):
        self.fail()