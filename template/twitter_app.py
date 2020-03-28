import twitter

consumer_key=" "
consumer_secret = " "
access_token= " "
access_secrets= " "

api = twitter.Api(consumer_key=consumer_key,
	consumer_secrets=consumer_secret,
	access_token_key=access_token,
	access_token_secret=access_secrets)

#gives us about the account details
print(api.VerifyCredentials())

#to print the followers
followers= api.GetFollowers()

#to print the friends

friends = api.GetFriends()

