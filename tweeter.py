import tweepy
from keys import apiKey, apiKeySecret, accessToken, accessTokenSecret


class Tweeter:
    def __init__(self, search_query, numTweets):
        self.search_query = search_query
        # Make sure we don't get more than 25 tweets
        if int(numTweets) > 25:
            numTweets = 25

        self.numTweets = numTweets
        self.api = self.authenticate()
        self.tweets = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return tweepy.API(auth)

    def scrapeTweets(self):
        cursor = tweepy.Cursor(
            self.api.search, q=self.search_query, tweet_mode="extended"
        )
        for tweet in cursor.items(self.numTweets):
            data = {
                "text": tweet.full_text,
                "date": tweet.created_at,
                "user": tweet.user.name,
                "url": "https://twitter.com/" + tweet.user.screen_name,
                "image": tweet.user.profile_image_url,
            }
            self.tweets.append(data)

    def getTweets(self):
        return self.tweets
