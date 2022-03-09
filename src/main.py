import configparser
import os
from recommender import Recommender


def _load_config() -> configparser.ConfigParser:
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    config_file = os.path.join(base_folder, "config.cnf")

    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        print(f"Config file missing... Path should be {config_file}")

    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')

    return config


def main():
    config = _load_config()

    rec = Recommender(config)

    playlist_id = rec.find_playlist_id("", "forest")
    print(playlist_id)
    song_ids = rec.get_songs("", playlist_id)
    print(song_ids)

    return 0


if __name__ == "__main__":
    main()
