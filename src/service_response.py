import json
from enum import Enum
from quack_location_type import QuackLocationType


class Errors(Enum):
    NoConfigFile = 105
    CouldNotInitializeRecommender = 109
    CouldNotInitializeSpotipy = 110
    CouldNotInitializeVectorSpace = 111
    CouldNotFindClosestTracks = 112
    CouldNotFindSongsFromPlaylist = 113
    CouldNotFormatSongListToJson = 114
    QuackLocationTypeArgumentNotANumber = 115
    QuackLocationTypeNotWithinRange = 116
    CouldNotFindTracksFromRangeRecommender = 117
    CouldNotInitializeRangeModel = 118
    CouldNotLoadDataSet = 119
    CouldNotInitializeVectorSpaceModel = 120
    Argument3NotGiven = 121
    Argument3NotARecommender = 122
    CouldNotLoadTrackData = 123
    CouldNotReadPrecalculatedDataSet = 124
    CouldNotTransformCSVIntoCorrectFormat = 125
    Argument4IncorrectFormat = 126
    Argument5NotANumber = 127
    NoTracksInTargetLocation = 128


def service_response_error_json(error_no: int):
    parsed_result = {
        "is_successful": 0,
        "error_no": error_no,
        "error_msg": Errors(error_no).name
    }
    return json.dumps(parsed_result, indent=4)


def service_response_playlist_json(tracks, location: QuackLocationType, offset: int):
    parsed_result = {
        "result": {
            "offset": offset,
            "location_type": location.value,
            "tracks": tracks
        },
        "is_successful": 1,
        "error_no": 0
    }
    return json.dumps(parsed_result)
