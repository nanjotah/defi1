# -*- coding: utf-8 -*-
##################################
# Twitter API interface
##################################

import tweepy


class twitter:
    
    def __init__(self):
        """        
        Initialisation de la classe, ne requiert aucun parametre (hard coded authentification)
        """
        self.auth_handler = tweepy.OAuthHandler("c9i3PW0gezoXzBuJVgqzZQ","veqwSzAPniNFQyHCtuCAb3ciqj0CbAw4Lef0BfmHoUM")
        self.auth_handler.set_access_token("2315490229-TwWACB6UUaqv8odiw7lwnVi5d8EnjUu8ADrFg9n","SoPToYmmtswjIE3UFE64NG1aXgm4gU36SMMB1fpofaIvN")
        self.twitter_api = tweepy.API(self.auth_handler)
    
    def search(self, hashtag_list):
        tweets_list = []
        if hashtag_list == [] or hashtag_list == "" or isinstance(hashtag_list,str) != True:
            print "Search field empty"
            return None
        
        for hashtag in hashtag_list:
            tweets_list.append(self.twitter_api.search("#%s" % hashtag))
        return tweets_list
            