import tweepy

# Create variables for each key, secret, token
consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET KEY'
access_token = 'YOUR ACCESS TOKEN'
access_token_secret = 'YOUR ACCESS TOKEN SECRET'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = 'Hello, world, this is a twitter application to tweet :-)'
api.update_status(status=tweet)
