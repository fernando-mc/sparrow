#!/usr/bin/env python

from ConfigParser import SafeConfigParser
from twython import Twython

#These values are all pulled from a file called 'config.ini'
#You can call yours myawesomebotconfig.ini or whatever else!
#Just remember to change it here

config_file_name = 'config.ini'

#SECURE YOUR CONFIG FILE - Don't put it in source code

parser = SafeConfigParser()
parser.read(config_file_name)

API_KEY = parser.get(config_file_name,'API_KEY') #AKA 'Consumer Key'
API_SECRET = parser.get(config_file_name,'API_SECRET') #AKA 'Consumer Secret'
ACCESS_TOKEN = parser.get(config_file_name,'ACCESS_TOKEN') #AKA 'OAUTH Token'
ACCESS_TOKEN_SECRET = parser.get(config_file_name,'ACCESS_TOKEN_SECRET') #AKA 'OAUTH Token Secret'

twitter = Twython(API_KEY, API_SECRET,
                  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def send_tweet(tweet_text):
    twitter.update_status(status = tweet_text)

send_tweet("This is my first tweet with Sparrow by @fmcorey - https://github.com/fmcorey/sparrow")
