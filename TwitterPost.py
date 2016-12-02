import tweepy
import time
import sys
import os

def sendTweet(tweet):

	consumer_key = 'AmnZ6ch3kVZcqxsKeSPuT87EF'
	consumer_Secret = 'ZEQVQImQvJqLS1p5BHdozlufLa5zcU0sKrfjIfzul5qeQHXjfy'
	access_token = '804723989209718784-6YlRysGsAO40fDXXPbJK4eaPWUQt4Ya'
	access_token_secret = 'x27J0TZdKGvtMiwhFt34DWtkRzLd5H7UFidRooY3GSSrl'

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
