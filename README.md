Repo for SoixanteCircuits Defi
===
Dependencies
------------
Two versions are provided.
First uses simple math to give approximate distance calculation (Haversine formula)
Second uses distance calculations from geopy package.
This script uses tweepy package to interface twitter OAuth system, it could be rewritten 
using standard python_oauthlib but this would imply more complex code

We chose tweepy against python-twitter because httplib2 which python-twitter will soon be replaced by new python-requests


geopy package can be found at https://github.com/geopy/geopy

tweepy package can be found at https://github.com/tweepy/tweepy