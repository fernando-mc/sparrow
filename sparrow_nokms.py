#!/usr/bin/env python
import random
import json
from twython import Twython

# Credentials setup
# Loads in 'creds.json' values as a dictionary
with open('creds.json') as f:
    credentials = json.loads(f.read())

# Sets config values from the config file
CONSUMER_KEY = credentials["consumer_key"]
CONSUMER_SECRET = credentials["consumer_secret"]
ACCESS_TOKEN_KEY = credentials["access_token_key"]
ACCESS_TOKEN_SECRET = credentials["access_token_secret"]

# Create the Twython Twitter client using our credentials
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# Sample random tweets
potential_tweets = [
    'This is my first tweet with Sparrow by @fmc_sea - https://github.com/fernando-mc/sparrow',
    'Wow! Isn\'t Sparrow by @fmcorey just the coolest! https://github.com/fernando-mc/sparrow',
    'Jeez! Everyone should learn about AWS Lambda and Twitter Bots from @fmc_sea'
]

def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""
    twitter.update_status(status = tweet_text)

def handler(event,context):
    """Sends random tweet from list of potential tweets"""
    send_tweet(random.choice(potential_tweets))



