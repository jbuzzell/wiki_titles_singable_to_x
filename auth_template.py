import tweepy

def auth():

    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""

    authorize = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authorize.set_access_token(access_key, access_secret)

    api = tweepy.API(authorize)

    return api