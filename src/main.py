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
    track = Track() # Metallica - Seek and Destroy
    track.danceability = 0.445
    track.energy = 0.964
    track.loudness = -5.493
    track.speechiness = 0.282
    track.acousticness = 0.037
    track.instrumentalness = 0.0132
    track.liveness = 0.0773
    track.valence = 0.448
    track.tempo = 140.817
    result = vsm.closest_tracks(track)
    for r in result:
        print(r.name, r.artists, r.vec)
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
