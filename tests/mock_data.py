import os
from configparser import ConfigParser
from typing import Optional


class MockData:
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self) -> Optional[ConfigParser]:
        base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        config_file = os.path.join(base_folder, "config_test.cnf")

        if not os.path.exists(config_file) or not os.path.isfile(config_file):
            return None

        config = ConfigParser()
        config.read(config_file, encoding='utf-8')

        return config

    def mock_find_songs(self):
        return """{ "result": { "id": "1987119c-5ab8-4f0b-a6de-8f42ddce527b", "location_type": "forest", "tracks": [{"id": "1Pcr11BvLJJldjWqpdDp2l","name": "All We Have Is Now","artist": "Ross Copperman","image": "https://i.scdn.co/image/ab67616d000048515fde2391a4d930feb4f976eb"}]},"is_successful": 1,"error_no": 0}"""