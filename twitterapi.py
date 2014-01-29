# -*- coding: utf-8 -*-
##################################
# Twitter API interface
##################################
import twitter
import requests,json

class Twitter:
    def __init__(self):
        self.api = twitter.Api(consumer_key="c9i3PW0gezoXzBuJVgqzZQ",\
                          consumer_secret="veqwSzAPniNFQyHCtuCAb3ciqj0CbAw4Lef0BfmHoUM",\
                              access_token_key="2315490229-TwWACB6UUaqv8odiw7lwnVi5d8EnjUu8ADrFg9n",\
                                  access_token_secret="SoPToYmmtswjIE3UFE64NG1aXgm4gU36SMMB1fpofaIvN")
        
    def streamgeotweets(self, hashtag):
        """ Performs a stream request to Twitter"""
        # AND search impossible for streaming
        hashtag = "#%s"%hashtag
        streamresults = self.api.GetStreamFilter(track=[term],locations=["-180,-90,180,90"])
        return streamresults
    
    def searchgeotweets(self,hashtag):
        """ Performs a Twitter search """
        a = []
        hashtag = "#%s"%hashtag
        results = self.api.GetSearch(term=hashtag, geocode = (48.856578, 2.351828,"10000km"))
        for i in results:
            if i.user.location != None:
                # As geotagged tweets are rare we try to find coordinates from user's location
                try:
                    geocoding = requests.get("http://maps.googleapis.com/maps/api/geocode/json", params = {
                        "address":"%s" % i.user.location,
                        "sensor":"false"}, proxies=None)
                except Exception as e : continue
                # If google api goes well
                if geocoding.status_code == 200:
                    try: 
                        geocodes = geocoding.json()["results"][0]["geometry"]["location"]
                        a.append({"tweet": i,"coordinates": [geocodes["lat"],geocodes["lng"]] })
                    except Exception as e : continue
                else: continue
        results = a
        return results
    
    def get10geotweetsfromstream(self, tweetstream):
        """ Get the first ten geotagged tweets from a twitter stream """
        i=0
        geotweets_list = []
        while i<10:
            tweet = tweetstream.next()
            try:
                if tweet['coordinates'] != None:
                    geotweets_list.append(tweet)
                    i = i+1
            except Exception as e:
                continue
        return geotweets_list
    
    