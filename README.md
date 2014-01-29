Repo for SoixanteCircuits Defi
===
Notes
-----
Searching for geotagged tweets can be done using the Twitter Search API or Streaming API.
While streaming API gives good geolocalization data it can't perform location AND term search.
But we can first gather data relative to the hashtag search and filter out the geolocalizable ones.
Search API provides good quality geolocalizable tweets and complex search capabilities but not all
tweets have coordinates so we must use the Google Maps API to retrieve coordinates from user's location name.
Two versions are provided : searchversion() and streamversion()


Dependencies
------------
geopy package can be found at https://github.com/geopy/geopy
python-twitter can be found at https://github.com/bear/python-twitter

This python script may need additional packages :
urllib, urllib2, requests, requests_oauthlib