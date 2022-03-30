import sys
from recommender import Recommender
from service_response import Errors, service_response_error_json
from quack_location_type import QuackLocationType
from spotify_requests import SpotifyRequests


def main(args):
    error_no = 0
    try:
        error_no = Errors.CouldNotInitializeSpotipy
        sr = SpotifyRequests(args[0])

        error_no = Errors.QuackLocationTypeArgumentNotANumber
        loc = int(args[1])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(loc)
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    rec = Recommender(sr)
    result = rec.get_playlist(location.name)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
