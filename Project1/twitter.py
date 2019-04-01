import re

import tweepy

from mapFolium import MapFolium

class TwitterAPI:

    def __init__(self):
        # user credentials to access Twitter API
        access_token = "1090251522473160705-sA7oi1AIiNTNJUl2A2PjGngijy44vy"
        access_secret = "qzIJ66jtiyxKHB0zwBhiifKSL4c9RLj2LGaHevnr92BuV"
        consumer_key = "dspktk1iXqA2yYHBrVkncPQw9"
        consumer_secret = "F323o3PI0UrO9ZvB4WWKx21QV3zxp1RrRF4aY4Rj1DR3beJCeL"

        # Setup tweepy to authenticate with Twitter credentials:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        # Create the api to connect to twitter with your creadentials
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    def getAPI(self):
        return self.api



class StreamListener(tweepy.StreamListener):
    def init(self):
        newMap = MapFolium()
        newMap.init()
        self.map = newMap

    def on_status(self, status):

        #with open("twitter_file.json", "a", encoding='utf-8') as write_file:
        #    if status.place != None:
        #        json.dump(status._json, write_file, ensure_ascii=False)
        #        write_file.write("\n")
        #        print(status.text)

        #Si le language du Tweeter est le francais alors on ajoute le mot à la liste de mot
        if(status._json.get("lang") == 'fr'):

            #On coupe la phrase en une liste de mot uniquement composés de lettres
            self.map.addWordsToTheMap(re.split("\\W", re.sub(r'http\S+', '', status.text)))
            self.map.saveMap()

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def useStreamByLocation(self, twitterAPI, location):
        tweetStream = tweepy.Stream(auth=twitterAPI.getAPI().auth, listener=self)
        tweetStream.filter(locations=location)