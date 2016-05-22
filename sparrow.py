#!/usr/bin/env python
import json
from twython import Twython

#This opens 'creds.json' and turns json into a Python array
with open('creds.json') as f:
    credentials = json.loads(f.read())

#This creates the Python Twitter client and uses our credentials
twitter = Twython(credentials["consumer_key"],
                  credentials["consumer_secret"],
                  credentials["access_token_key"],
                  credentials["access_token_secret"])

def send_tweet(tweet_text):
    twitter.update_status(status = tweet_text)

send_tweet("This is my first tweet with Sparrow by @fmcorey - https://github.com/fmcorey/sparrow")
