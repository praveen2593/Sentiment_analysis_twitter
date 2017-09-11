import tweepy
import time
import numpy as np
from pymongo import MongoClient
import settings

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            with open('tweets_no_filter.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: {}".format(str(e)))
            time.sleep(5)
        return True

    def on_error(self, status):
        print status
        return True


class TWITTER(object):
    def __init__(self):
        self.auth = None
        self.tweet_stream = None
        pass

    def _authenticate(self):
        self.auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
        self.auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)

    def load_data(self, auth = 0):
        if auth == 0:
            self._authenticate()
        self.api = tweepy.API(self.auth)
        return tweepy.Stream(self.auth, MyStreamListener())

if __name__ == '__main__':
    tweet = TWITTER()
    twet = tweet.load_data()
    twet.filter(track=['Neymar_Jr'] , languages=['en'])
