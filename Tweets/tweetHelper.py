from tweepy import OAuthHandler
import json, datetime, time, timestring
import tweepy, os, csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FluDjango.settings")
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'filter.txt')
file_path2 = os.path.join(module_dir, 'subunits.csv')
# import Tweets.models as model
from nltk.tokenize import word_tokenize

count = 0

# def analysis(tweet):
#     symptoms = ['cough', 'fever','sick'] # need a better way to do this. shold probably write this into a json and read it when analyzing
#     tweet_score = 0
#
#     words = word_tokenize(tweet)
#     #tagged_words = nltk.pos_tag(words) # not sure what to use this for yet, but I think it's at least cool to have
#     for word in words:
#         tweet_score = tweet_score + symptomRecognition(word, symptoms)
#
#     return tweet_score
#
# def symptomRecognition(word, symptoms):
#     symptoms1 = [symptoms[0], symptoms[1]]
#     symptoms2 = [symptoms[2]]
#     if word.lower() in symptoms1: # check lowercase word
#         return 1
#     if word.lower() in symptoms2:
#         return 0.5
#     return 0
#
# def regionCreator():
#     with open(file_path2) as f:
#         reader = csv.reader(f)
#         for col in reader:
#             reg, created = model.Region.objects.get_or_create(
#                 subunit=int(col[0]),
#                 location=str(str(col[1])+","+str(col[2])+","+str(col[3]))
#                 )
#
#
# def write_tweets(api, filter, count):
#     page = 1
#     ct = 0
#     deadend = False
#     regions = model.Region.objects.all()
#     for reg in regions:
#         tweets = tweepy.Cursor(api.search, q=filter, geocode=reg.location).items(count)
#         for tweet in tweets:
#             t, created = model.Tweet.objects.get_or_create(
#                 content=tweet.text,
#                 user=tweet.user.screen_name,
#                 date=tweet.created_at,
#                 region=reg)
#             ct = ct + 1
#
#             # exit clause
#             if ct == count:
#                 continue
#             #else:
#             #    deadend = True
#             #    return
#         if not deadend:
#             page+=1
#             time.sleep(500)

def print_tweets(api, filter, count):
    page = 1
    ct = 0
    deadend = False
    # regions = model.Region.objects.all()
    # for reg in regions:
    #     print(reg.location)
    while True:
        # run api search
        tweets = tweepy.Cursor(api.search, q=filter, geocode="40.719,-73.987,3km").items(count)
        for tweet in tweets:
            print(tweet.text)
            ct = ct + 1

            # exit clause
            if ct == count:
                return

        if not deadend:
            page+=1
            time.sleep(500)


def tweetPull():
    # regionCreator()

    # First API stuff
    # access_token = "97325888-4TiheE2EDlLRrRd0i3RyL99uIRMIjqOgMJilVWxsO"
    # access_token_secret = "pHpBZnMavx1lTGA1UnS6Uzs6VvLJuwIBP7ExYXqbozoqg"
    # consumer_key = "BuAsYJarW7WleTg0PrsvrrF2O"
    # consumer_secret = "REOFH6Ue0vewobC1WILncfQrweqPIHc94JTjCBh3iuPhkckYPz"
    # Second API stuff
    # access_token = "3506626817-Kt7S6hZRUYlpQaqVzIEJ0d9I0UUpmRFEIVlWGMK"
    # access_token_secret = "z5jKWniIAGNT9xCezjIKEYdoe8IvKd764oVbQHbaIBI3V"
    # consumer_key = "90UdIH7EzK6Zxq40nszhKrHIm"
    # consumer_secret = "tcUtSpb1nj6XgKnMgMhpeelXXoVIshlJNqVorPemGGlyN9RtTd"
    # Third API stuff
    access_token = "97325888-USvE5Eh5o8zTO0kYYxRsgDb6De1jsUj5b7dwArH0I"
    access_token_secret = "POz3D5g7QlTILsnGwIXG8jDrugpKIUhyje7UWjOGs6h5I"
    consumer_key = "POBbYmryu4AudDxSGH1xMvzt1"
    consumer_secret = "2mfK8DOry5vIn1f50DRBMksm7U9WE7lbxbfFcBPgQYwjQvCfbC"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # filter words (array named "filter")
    file = open(file_path) # read in filter words from file named "filter.txt"; alter that file or just write it in here
    filter = file.readlines()
    query = ""
    file.close()
    for x in range(0, len(filter) - 1):
        query += filter[x].strip() + " OR "
    query += filter[len(filter) - 1]
    print(query)

    # desired number of tweets
    count = 20

    ''' run function '''
    #write_tweets(api,filter,start_date,end_date,region,count)
    print_tweets(api, query, count)

def test():
    global count
    if count == 0:
        print("test")
    count = 1

tweetPull()