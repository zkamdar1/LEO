# post_tweet.py

import os
import tweepy
import logging
from dotenv import load_dotenv
from generate_tweet import generate_tweet  # Import the generate_tweet function

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='post_tweet.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Twitter Authentication
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

auth = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

def post_tweet():
    """
    Generates a tweet and posts it to Twitter.
    """
    tweet = generate_tweet()
    if tweet:
        # Ensure tweet length is within Twitter's limit
        if len(tweet) > 280:
            tweet = tweet[:277] + '...'

        try:
            auth.create_tweet(text=tweet)
            logging.info(f"Tweet posted: {tweet}")
            print(f"Tweet posted: {tweet}")
        except Exception as e:
            logging.error(f"Error posting tweet: {e}")
            print(f"Error posting tweet: {e}")
    else:
        logging.info("No valid tweet generated. Skipping post.")
        print("No valid tweet generated. Skipping post.")

if __name__ == "__main__":
    post_tweet()
