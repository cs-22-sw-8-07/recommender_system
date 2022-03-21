import configparser
import os
import sys, getopt
from configparser import ConfigParser
from typing import Optional
from recommender import Recommender
from enum import Enum


class QuackLocationType(Enum):
    unknown = 0
    church = 1
    education = 2
    cemetery = 3
    forest = 4
    beach = 5
    urban = 6
    night_life = 7


def _load_config() -> Optional[ConfigParser]:
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    config_file = os.path.join(base_folder, "config.cnf")

    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        print(f"Config file missing... Path should be {config_file}")
        return None

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    return config


def main(args):
    config = _load_config()
    if config is None:
        return 0

    location = QuackLocationType(int(args[1]))

    rec = Recommender(config)
    rec.connect_spotify(args[0])
    playlist_id = rec.find_playlist_id(location.name)
    songs_json = rec.get_songs(playlist_id)
    print(songs_json)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
