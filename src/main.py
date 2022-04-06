import os
import sys
from configparser import ConfigParser
from typing import Optional
from feature_vector import FeatureVector
from range_model import RangeModel
from recommender import Recommender
from service_response import Errors, service_response_error_json
from quack_location_type import QuackLocationType
from track_data import TrackData
from vector_space_model import VectorSpaceModel


def load_config() -> Optional[ConfigParser]:
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    config_file = os.path.join(base_folder, "config.cnf")

    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        return None

    config = ConfigParser()
    config.read(config_file, encoding='utf-8')

    return config


def main(args):
    config = load_config()

    # Test block
    range_model = RangeModel()
    # Test block

    error_no = 0
    try:
        error_no = Errors.CouldNotInitializeVectorSpace
        feature_vec = FeatureVector()

        vsm = VectorSpaceModel()
        vsm.load_csv(config.get('VECTOR_SPACE_MODEL', 'path_csv'))

        error_no = Errors.QuackLocationTypeArgumentNotANumber
        loc = int(args[1])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(loc)
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    rec = Recommender(feature_vec, vsm)
    result = rec.get_playlist(location.name)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
