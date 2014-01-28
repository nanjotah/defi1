# -*- coding: utf-8 -*-
#########################
# Tweets around Paris
#########################

import utils
import sys
from twitterapi import twitter
import argparse

def args_parse():
    """
    This function parses command line arguments we should pass to the script
    """
    # Arguments definition and help
    parser = argparse.ArgumentParser(description = "Returns tweets and their geolocalized distances from Paris.")
    parser.add_argument("hashtag", metavar = '#hashtag', type=str, nargs='?', help='Twitter hashtag to look for (without # sign)')
    args = parser.parse_args()
    # If no argument is provided the script exits otherwise it returns correctly formatted arguments
    if args.hashtag == None : 
        print "You must specify a search term, otherwise nothing can be searched"
        sys.exit()
    else :
        return args
    
    
if __name__ == "__main__" :
    """
    Main function
    """
    # Argument parsing
    args = args_parse()
    # Twitter session initialisation
    twit_app = twitter()
    # Twitter search
    tweets_list = twit_app.search("%s"%args.hashtag)
    print tweets_list
    