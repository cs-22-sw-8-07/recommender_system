import sys
from recommender import Recommender
from service_response import Errors, service_response_error_json
from quack_location_type import QuackLocationType
from spotify_requests import SpotifyRequests
from vector_space_model import VectorSpaceModel, Track


def main(args):
    # Test block
    vsm = VectorSpaceModel()
    vsm.load_csv(r"C:\Users\Jeppe\Downloads\archive\tracks.csv")
    track = Track()
    track.danceability = 0.298
    track.energy = 0.46
    track.loudness = -18.645
    track.speechiness = 0.453
    track.acousticness = 0.521
    track.instrumentalness = 0.856
    track.liveness = 0.436
    track.valence = 0.402
    track.tempo = 87.921
    result = vsm.closest_tracks(track)
    return 0
    # Test block


    error_no = 0
    try:
        error_no = Errors.CouldNotInitializeSpotipy
        sr = SpotifyRequests(args[0])

        error_no = Errors.QuackLocationTypeNotWithinRange
        location = QuackLocationType(int(args[1]))
    except:
        print(service_response_error_json(error_no.value))
        sys.exit()

    rec = Recommender(sr)
    result = rec.get_playlist(location.name)
    print(result)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
