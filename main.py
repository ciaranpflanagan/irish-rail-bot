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

def get_percentage(target_account, number_tweets):
	# Getting User
	keywords = ['delays','delay', 'mechanical problem', 'emergency services', 'currently stopped', 'canceled', 'behind schedule', 'transferred', 'alternative service', 'fault', 'bus transfers', 'issue', 'disruptions', 'being held', 'service suspended', 'late', 'stopped']
	tweet_found = 0
	reply = 0
	item = auth_api.get_user(target_account)
	for status in Cursor(auth_api.user_timeline, id=target_account).items(number_tweets):
		# Filtering out replies to only include tweets
		if (status.in_reply_to_status_id is None):
			# If one of the keywords is found, increment counter
			if any(substring in status.text.lower() for substring in keywords):
				tweet_found += 1
			else:
				print(status.text + '\n')
		else:
			reply += 1
	print("Tweets containing delays = " + str((tweet_found / (number_tweets - reply)) * 100) + "%")

get_percentage('IrishRail', 1000)