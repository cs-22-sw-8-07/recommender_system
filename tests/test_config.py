from unittest import TestCase
from config import load_config


class TestConfig(TestCase):
    def setUp(self):
        pass

    def test_load_config__test_config(self):
        load_config("test_config.cnf")

    def test_load_config__unknown_config(self):
        try:
            load_config("unknown_config.cnf")
        except:
            return

        self.fail()
