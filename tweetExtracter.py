import sys
import csv

import argparse
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "XXXXX"
consumer_secret = "XXXXX"
access_key = "XXXXX"
access_secret = "XXXXX"


def getTweets(username,noOfTweets):
	"""
	parameter: 
		username - useranem of the twitter handle 
		noOfTweets - number of twwets we want to extract
	
	Get the tweets and save it in csv file.
	In current Working Directory
	"""
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	if noOfTweets is None:
		tweets_for_csv = []
		for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items():
			#create array of tweet information: username, tweet id, date/time, text
			tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
	else:
		tweets_for_csv = []
		for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(noOfTweets):
			#create array of tweet information: username, tweet id, date/time, text
			tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

	#Write the tweets list to csv file.
	fileName = username + "_tweets.csv"
	with open(fileName, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)
	
	print('@'+username+" Tweets Save in "+fileName)

if __name__ == '__main__':
	"""
	Get the username and number of tweets to extract from the command line
	"""
	try:
		#Get the username and number of tweets from command line
		parser = argparse.ArgumentParser(description='Pass the username and the number of tweets')
		parser.add_argument('--username',nargs='+')
		parser.add_argument('--number_of_tweets',type=int)

		args = parser.parse_args()
		userName = args.username
		noOfTweets = args.number_of_tweets

		if len(userName) == 1:
			getTweets(userName,noOfTweets)
		else:
			for user in userName:
				getTweets(user,noOfTweets)

	except Exception as ex:
		print("An error occurred: " + str(ex))
	