# Imports
from datetime import date
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json

# Twitter API authentification
consumer_key = 'Hbn0ISayL2SZKu8hn7VKXWoII'
consumer_secret = 'FJcWqAeGZ0fTnAJfd2NfOAW98qE0WwhToB74yM1yfjhCxAVGjH'
access_token = '1322874566960709636-lb6RbAQgutNd4Ck5AI5ewjRBopXVx1'
access_secret = '2iGnXulknfSjrxV6wh3pA38ycLZvnJ1HwJixKITNzycxl'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Variables to filter specific tweets
location = []

languages = ['en']  # Deutsche und Englische Tweets werden gesucht

track = ['#Azure', '#Datalake', '#Microsoft', '#Analysis', '#cloud']


# Stream-Listener saves live tweets into JSON file according to specific filters
class Listener(StreamListener):
    1 == 1;


class ListenerChild(Listener):

    def on_data(self, data):
        try:
            with open('liveTweetsRaw.json', 'a') as file:
                file.write(data)
        except KeyError:
            logging.info("rate limited" + date.today().strftime('%Y-%m-%d %H:%M:%S'))

    def on_error(self, status):
        print(status)


stream = Stream(auth=auth, listener=ListenerChild(api=None), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

stream.filter(locations=location, languages=languages, track=track)