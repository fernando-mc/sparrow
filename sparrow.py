#!/usr/bin/env python
import json
from twython import Twython

#These values are all pulled from a file called 'config.ini'
#You can call yours myawesomebotconfig.ini or whatever else!
#Just remember to change it here

with open('creds.json') as f:
    credentials = json.loads(f.read())

#SECURE YOUR CONFIG FILE - Don't put it in source code

twitter = Twython(credentials["consumer_key"],
                  credentials["consumer_secret"],
                  credentials["access_token_key"],
                  credentials["access_token_secret"])

def send_tweet(tweet_text):
    twitter.update_status(status = tweet_text)

send_tweet("This is my first tweet with Sparrow by @fmcorey - https://github.com/fmcorey/sparrow")
