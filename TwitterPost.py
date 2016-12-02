import tweepy
import time
import sys
import os

def sendTweet(tweet):

	consumer_key = 'Regular Key'
	consumer_Secret = 'SecretKey'
	access_token = 'Access_token'
	access_token_secret = 'Access_Secret'

	myTweet = input("Please tell me what you wanna tweet: " )

	auth = tweepy.OAuthHandler(consumer_key, consumer_Secret)
	auth.set_access_token(access_token,access_token_secret)
	auth.secure = True
	api = tweepy.API(auth)
	if tweet==[]:
		tweet = (myTweet)
	print("tweeting now: ", tweet)
	api.update_status(tweet)

if __name__ == '__main__':
	myTweet = input("Please tell me what you want to tweet: ")
	sendTweet(myTweet)
