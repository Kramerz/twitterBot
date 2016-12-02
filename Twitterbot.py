import tweepy
import random
from time import sleep

consumer_key = 'AmnZ6ch3kVZcqxsKeSPuT87EF'
consumer_Secret = 'ZEQVQImQvJqLS1p5BHdozlufLa5zcU0sKrfjIfzul5qeQHXjfy'

access_token = '804723989209718784-6YlRysGsAO40fDXXPbJK4eaPWUQt4Ya'
access_token_secret = 'x27J0TZdKGvtMiwhFt34DWtkRzLd5H7UFidRooY3GSSrl'


auth = tweepy.OAuthHandler(consumer_key, consumer_Secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

myBot = api.get_user(screen_name = '@DearRyanW')
myList = api.get_list("@"+myBot.screen_name, slug ='sorry-for-adding-you')

print("Running bot: @" + myBot.screen_name + "\n Using List: " + myList.name + " \n Members count: " + str(myList.member_count) + "Subs Count: "+ str(myList.subscriber_count))

for tweet in tweepy.Cursor(api.search,q = '#Python', lang='en').items(2):
#print(str(api.get_user(screen_name = '@DearRyanW')))').items(5):
	try:
		if tweet.user.id == myBot.id:
			continue
		print("\nFound tweet by: @" + tweet.user.screen_name)
		if (tweet.retweeted == False) or (tweet.favorited == False):
			tweet.retweet()
			tweet.favorite()
			api.add_list_members(screen_name = tweet.user.screen_name, owner_screen_name = myBot.screen_name, list_id= myList.id)
			print("Retweented, favorited, and added user to the list for the tweet of: " + tweet.user.screen_name)
		if(tweet.user.following == False):
			tweet.user.follow()
			print("You're now following: @" + tweet.user.screen_name)			
	except tweepy.TweepError as e:
		print(e.reason)
		sleep(5)
		continue
	except StopIteration: 
		break	

api.update_status(status='this is just a test')