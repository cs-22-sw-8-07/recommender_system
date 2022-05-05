# recommender_system

To customize the config file and make it point at the correct file in your filesystem, add the following line to (hidden folder) `.git/info/exclude` :

```
config.cnf
```

And then run the following command:

```
git update-index --assume-unchanged config.cnf
```

To get the kaggle dataset, download it from our shared drive folder under "Resourcer", or download it directly from kaggle: 
https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=tracks.csv

test_config.cnf is a config file used explicitly for the unit and integration tests. It is not neccessary to change the values in test_config.cnf, unless you are updating the tests.

## Arguments

The format for the arguments of the script is as follows:

```
<access_token> <location_type> <recommender_method> <previous_offsets> 
```

Formats:
* `access_token`: A string token for Spotify access
* `location_type`: An integer value for location
* `recommender_method`: A string that denotes which recommender method to use. Available values are `distance`, `range` and `machine`
* `previous_offsets`: (Optional) A list of integers of the format `0;1;2`. Denotes which page offsets have already been returned to the requesting client.