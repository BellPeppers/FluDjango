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

def write_tweets(api, filter, start_date, end_date, region, count):
    page = 1
    ct = 0
    deadend = False
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search, q=filter, lang="en", locations=region,since=start_date, until=end_date).items(count)
        for tweet in tweets:
            #if (datetime.datetime.now() - tweet.created_at).days < 5: # example time stamp: 2015-11-24 02:13:33 or 2015-11-01
            #    #Do processing here:
            #    #print tweet.geocode
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

def print_tweets(api, filter, start_date, end_date, region, count):
    page = 1
    ct = 0
    deadend = False
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search, q=filter, lang="en", locations=region,since=start_date, until=end_date).items(count)
        for tweet in tweets:
            #if (datetime.datetime.now() - tweet.created_at).days < 5: # example time stamp: 2015-11-24 02:13:33 or 2015-11-01
            #    #Do processing here:
            #    #print tweet.geocode
            print(tweet.text)
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
    file.close()
    for x in range(0, len(filter)):
        filter[x] = filter[x].strip()

    # dates to search within
    start_date = "2016-1-01" # year-mo-dy format
    end_date = "2016-02-19"

    # area of search
    region = [41.65,-79.67,44.91,-73.39] # set using coordinates (I think this is the state of New York atm)

    # desired number of tweets
    count = 20

    # json file to write to (if writing to file)
    json_file = 'tweets.json'

    ''' run function '''
    write_tweets(api,filter,start_date,end_date,region,count)
    #print_tweets(api, filter, start_date, end_date, region, count)
    #write_tweets_to_json(api, filter, start_date, end_date, region, count, json_file)
