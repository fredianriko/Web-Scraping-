
import tweepy
import json
import re



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

stream_listener = StreamListener(api)
stream = tweepy.Stream(auth=api.auth, listener=stream_listener, tweet_mode='streaming')

stream.filter(track=['python'+'language'])
