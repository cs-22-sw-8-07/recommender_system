import sys
from feature_vector import FeatureVector
from recommender import Recommender
from service_response import Errors, service_response_error_json
from quack_location_type import QuackLocationType


def main(args):
    # Test block
    args = ["BQD6BivurQGnmIeJ3CrnBuUxKelc_Z-KCQWWymkTigilwXtgzfNyCzQbYmZxVkwXDJOE2jK6k-c_A8mattgxArDMfWcU5wY4nHsvKMT-KVvJi3FSev1njMOVIiVoBQQR2lgh1FD79xd1G2l89bL25uTmVlVqrFxC","4" ]
    # Test block
    error_no = 0
    try:
        error_no = Errors.CouldNotInitializeSpotipy
        feature_vec = FeatureVector()

        error_no = Errors.QuackLocationTypeArgumentNotANumber
        loc = int(args[1])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(loc)
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    rec = Recommender(feature_vec)
    result = rec.get_playlist(location.name)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
