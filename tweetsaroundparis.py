# -*- coding: utf-8 -*-
#########################
# Tweets around Paris
#########################

import utils
import sys
from twitterapi import Twitter
import argparse
from operator import itemgetter

def args_parse():
    """ Parses command line arguments """
    parser = argparse.ArgumentParser(description = "Returns tweets and their geolocalized distances from Paris.")
    parser.add_argument("hashtag", metavar = '#hashtag', type=str, nargs='?', help='Twitter hashtag to look for (without # sign)')
    args = parser.parse_args()
    if args.hashtag == None : 
        print "You must specify a search term, otherwise nothing can be searched"
        sys.exit()
    else :
        return args
    
def tweetstream_arrange_by_distance_from_paris(tweets_list):
    """ Sorts the tweetstream list """
    tweets_distance = []
    for i,tweet in enumerate(tweets_list) :
        tweets_distance.append({
            'tweet':tweet,
            'distance':utils.distance_from_paris_geopy(tweet['coordinates']['coordinates'])
            })
    tweets_arranged = sorted(tweets_distance, key=itemgetter('distance'))
    return tweets_arranged

def tweetsearch_arrange_by_distance_from_paris(tweets_list):
    """ Sorts the tweetsearch list """
    tweets_distance = []
    for i in tweets_list:
        tweets_distance.append({
            "tweet":i["tweet"],
            "distance":utils.distance_from_paris_geopy(i["coordinates"])
            })
    tweets_arranged = sorted(tweets_distance, key=itemgetter('distance'))
    return tweets_arranged
    
def streamversion():
    """ The main program using stream API """
    # Argument parsing
    args = args_parse()
    # Twitter session initialisation
    twit_app = Twitter()
    # Twitter search
    tweets_stream = twit_app.streamgeotweets(args.hashtag)
    search_results = twit_app.get10geotweetsfromstream(tweets_stream)
    tweets_list_sorted = tweetstream_arrange_by_distance_from_paris(search_results)
    for i in tweets_list_sorted :
        print "TWEET: %s\nDISTANCE: %skm"%(i['tweet']["text"],i['distance'])

def searchversion():
    """ The main program using Search API """
    # Argument parsing
    args = args_parse()
    # Twitter session initialisation
    twit_app = Twitter()
    # Twitter search
    tweets_search = twit_app.searchgeotweets(args.hashtag)
    # Distances
    tweets_list_sorted = tweetsearch_arrange_by_distance_from_paris(tweets_search)
    for compte,i in enumerate(tweets_list_sorted) :
        if compte < 10:
            print "TWEET: %s\nDISTANCE: %skm"%(i['tweet'].text,i['distance'])
    
if __name__ == "__main__" :
    """
    Main function 
    """
    searchversion()
    
        