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
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

    # Test block
    args = ["asd", "4", "distance"]
    # Test block

    try:
        error_no = Errors.NoConfigFile
        config = load_config()

        error_no = Errors.QuackLocationTypeArgumentNotANumber
        loc = int(args[1])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(loc)

        error_no = Errors.Argument3NotGiven
        match args[2]:
            case "distance":
                error_no = Errors.CouldNotInitializeVectorSpace
                feature_vec = FeatureVector()
                path = os.path.join(base_folder, "resources", "allLocationFeatureVector.csv")
                feature_vec.load_feature_vectors(path)

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
            case _:
                error_no = Errors.Argument3NotARecommender
                raise Exception("Argument3NotARecommender")
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    result = rec.get_playlist(location)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
