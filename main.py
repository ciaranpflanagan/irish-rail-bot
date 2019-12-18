import os
import pandas as pd
import creds
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

# Credentials (pulled from creds.py)
consumer_key = creds.consumer_key
consumer_secret = creds.consumer_secret
access_token = creds.access_token
access_token_secret = creds.access_token_secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

# Get User
target = 'IrishRail'
keywords = ['delays','delay', 'mechanical problem', 'emergency services', 'currently stopped', 'cancelled', 'behind schedule']
tweet_no = 0
reply = 0
item = auth_api.get_user(target)
for status in Cursor(auth_api.user_timeline, id=target).items(10000):
	if any(substring in status.text.lower() for substring in keywords):
		if (status.in_reply_to_status_id is None):
			print(status.text + '\n')
			tweet_no += 1
		else:
			# Tweet is a reply
			reply += 1
print("Percentage % = ")
print(tweet_no / (10000 - reply))