from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, datetime, time, timestring
import tweepy
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FluDjango.settings")
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'filter.txt')
import Tweets.models as model

def write_tweets(api, filter, count):
    page = 1
    ct = 0
    deadend = False
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search, q=filter).items(count)
        for tweet in tweets:
            t, created = model.Tweet.objects.get_or_create(
                content=tweet.text,
                user=tweet.user.screen_name,
                date=tweet.created_at)
            ct = ct + 1

            # exit clause
            if ct == count:
                return
            #else:
            #    deadend = True
            #    return
        if not deadend:
            page+=1
            time.sleep(500)

def print_tweets(api, filter, count):
    page = 1
    ct = 0
    deadend = False
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search,q=filter).items(count)
        for tweet in tweets:
            print(tweet.text)
            print(tweet.place)
            print(tweet.coordinates)
            print(tweet.created_at)
            ct = ct + 1

            # exit clause
            if ct == count:
                return
            #else:
            #    deadend = True
            #    return
        if not deadend:
            page+=1
            time.sleep(500)


def tweetPull():
    # API stuff
    access_token = "97325888-4TiheE2EDlLRrRd0i3RyL99uIRMIjqOgMJilVWxsO"
    access_token_secret = "pHpBZnMavx1lTGA1UnS6Uzs6VvLJuwIBP7ExYXqbozoqg"
    consumer_key = "BuAsYJarW7WleTg0PrsvrrF2O"
    consumer_secret = "REOFH6Ue0vewobC1WILncfQrweqPIHc94JTjCBh3iuPhkckYPz"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # filter words (array named "filter")
    file = open(file_path) # read in filter words from file named "filter.txt"; alter that file or just write it in here
    filter = file.readlines()
    query = ""
    file.close()
    for x in range(0, len(filter)):
        query += filter[x].strip() + " OR "
    query += filter[len(filter) - 1]

    # area of search
    region = "37.781157,-122.398720,1mi" # set using coordinates (I think this is the state of New York atm)

    # desired number of tweets
    count = 20

    ''' run function '''
    #write_tweets(api,filter,start_date,end_date,region,count)
    print_tweets(api, query, count)
