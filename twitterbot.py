import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

tweet = '\n'.join(lines)

try:
    api.update_status(tweet)
except tweepy.TweepError as e:
    print (e.reason)



