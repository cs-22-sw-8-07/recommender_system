import os
import sys
from configparser import ConfigParser
from service_response import Errors, service_response_error_json
from quack_location_type import QuackLocationType
from range_model.range_model import RangeModel
from distance_model.feature_vector import FeatureVector
from distance_model.vector_space_model import VectorSpaceModel
from distance_model.distance_recommender import DistanceRecommender
from range_model.range_recommender import RangeRecommender


def load_config() -> ConfigParser:
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    config_file = os.path.join(base_folder, "config.cnf")

    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        raise Exception("No config file")

    config = ConfigParser()
    config.read(config_file, encoding='utf-8')

    return config


def main(args):
    error_no = 0

    try:
        error_no = Errors.NoConfigFile
        config = load_config()

        # Test block
        args = ["range", "5"]
        # Test block

        error_no = Errors.QuackLocationTypeArgumentNotANumber
        loc = int(args[1])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(loc)

        match args[0]:
            case "distance":
                error_no = Errors.CouldNotInitializeVectorSpace
                feature_vec = FeatureVector()

                error_no = Errors.CouldNotInitializeVectorSpaceModel
                vsm = VectorSpaceModel()
                vsm.load_csv(config.get('RECOMMENDER', 'dataset_csv'))

                error_no = Errors.CouldNotInitializeRecommender
                rec = DistanceRecommender(feature_vec, vsm)
            case "range":
                error_no = Errors.CouldNotInitializeRangeModel
                range_model = RangeModel(config)

                error_no = Errors.CouldNotLoadDataSet
                range_model.load_track_csv(config.get('RECOMMENDER', 'dataset_csv'))

                error_no = Errors.CouldNotInitializeRecommender
                rec = RangeRecommender(range_model)
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    result = rec.get_playlist(location)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
