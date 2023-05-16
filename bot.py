import tweepy
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
import requests
import random
import time
import sys
import openai
import textwrap

# Accessing credentials from .env file
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Setting credentials to access Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Calling API using Tweepy
api = tweepy.API(auth, wait_on_rate_limit=True)

# Search keyword
search = '#Bitcoin OR Bitcoin OR bitcoin OR #bitcoin'
# Maximum limit of tweets to be interacted with
maxNumberOfTweets = 1000000

# To keep track of tweets published
count = 0

print("Retweet Bot Started!")

for tweet in tweepy.Cursor(api.search_tweets, search).items(maxNumberOfTweets):
    try:
        # for each status, overwrite that status by the same status, but from a different endpoint.
        status = api.get_status(tweet.id_str, tweet_mode='extended')
        if status.favorited == False:
            print("###############################################################")
            print("Found tweet by @" + tweet.user.screen_name)
            tweet.favorite()
            print("Liked tweet")

            timeToWait = random.randint(3, 19)
            print("Waiting for " + str(timeToWait) + " seconds")
            for remaining in range(timeToWait, -1, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rOnwards to next tweet!\n")

    except tweepy.errors.TweepyException as e:
        print(str(e))
