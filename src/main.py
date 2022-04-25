import os
import sys
from config import load_config
from precalculated_recommender import PrecalculatedRecommender
from service_response import Errors, service_response_error_json
from quack_location_type import QuackLocationType


def main(args):
    error_no = 0
    amount = 10
    offset = 0

    try:
        error_no = Errors.NoConfigFile
        config = load_config("config.cnf")

        error_no = Errors.QuackLocationTypeArgumentNotANumber
        loc = int(args[1])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(loc)

        error_no = Errors.Argument3NotGiven
        match args[2]:
            case "distance" | "range":
                error_no = Errors.CouldNotInitializeRecommender
                rec = PrecalculatedRecommender(args[2])
            case _:
                error_no = Errors.Argument3NotARecommender
                raise Exception("Argument3NotARecommender")

        error_no = Errors.Argument4NotANumber
        if len(args) > 2:
            amount = int(args[3])

        error_no = Errors.Argument5NotANumber
        if len(args) > 3:
            offset = int(args[4])
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    result = rec.get_playlist(location, amount, offset)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
