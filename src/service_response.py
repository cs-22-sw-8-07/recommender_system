import json
from enum import Enum


class Errors(Enum):
    CouldNotInitializeSpotipy = 110
    CouldNotFindPlaylists = 111
    CouldNotFindSongsFromPlaylist = 112
    CouldNotFormatSongListToJson = 113


def service_response_error_json(error_no):
    parsed_result = {
        "is_successful": 0,
        "error_no": error_no
    }
    return json.dumps(parsed_result, indent=4)
