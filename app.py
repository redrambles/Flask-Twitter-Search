from flask import Flask, render_template
from tweeter import Tweeter

app = Flask(__name__)


search_term = input("What shall we search Twitter for? ")
tweet_number = input("How many tweets? (1-25) ")

int_tweet_number = int(tweet_number)
tweetObject = Tweeter(search_term, int_tweet_number)
tweetObject.scrapeTweets()
tweetResults = tweetObject.getTweets()


@app.route("/")
def homepage():
    return render_template("index.html", tweets=tweetResults, search_term=search_term)
