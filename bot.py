import os
import tweepy
import openai
import schedule
import time
from dotenv import load_dotenv
import logging
import random

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Twitter API credentials from environment variables
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)
api = tweepy.API(auth)

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

# Define the bot's persona and rules
BOT_NAME = "Leo aka Jamaal Saab"
ANIMAL = "orange cat named ^"

# Define a list of content types
CONTENT_TYPES = [
    "advice",
    "joke",
    "one-liner",
    "serious reflection",
    "fun fact",
    "motivational quote",
    "short story",
    "crypto tip",
    "stock market insight",
    "political commentary",
    "random thought",
    "humorous observation"
]

def generate_tweet():
    # Select a random content type
    content_type = random.choice(CONTENT_TYPES)
    
    # Define the rule components
    who = BOT_NAME
    what = content_type
    why = "to engage followers and grow the community"

    # Craft the prompt
    prompt = (
        f"Rule:\n"
        f"Who: {who}\n"
        f"What: {what}\n"
        f"Why: {why}\n\n"
        f"Prompt:\n"
        f"Generate a unique and natural-sounding tweet by {ANIMAL} about {what}. "
        f"The tweet should be {random.choice(['short', 'medium', 'long'])} in length and written in a {random.choice(['playful', 'serious', 'humorous', 'informative', 'inspirational'])} style. "
        f"Ensure proper grammar, syntax, and structure. Occasionally, subtly hint at an upcoming memecoin to build interest."
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or use the appropriate model
            prompt=prompt,
            max_tokens=100,  # Adjust as needed
            temperature=0.7,
            n=1,
            stop=None,
        )
        tweet = response.choices[0].text.strip()
        return tweet
    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return None

def post_tweet():
    tweet = generate_tweet()
    if tweet:
        # Ensure tweet length is within Twitter's limit
        if len(tweet) > 280:
            tweet = tweet[:277] + '...'
        
        try:
            api.update_status(tweet)
            logging.info(f"Tweet posted: {tweet}")
            print(f"Tweet posted: {tweet}")
        except tweepy.TweepError as e:
            logging.error(f"Error posting tweet: {e}")
            print(f"Error posting tweet: {e}")
    else:
        logging.error("Failed to generate tweet. Skipping post.")
        print("Failed to generate tweet. Skipping post.")

def main():
    # Schedule the tweet at 7:00 PM every day
    schedule.every().day.at("19:00").do(post_tweet)

    logging.info("Twitter bot started and scheduled to post daily at 7:00 PM.")
    print("Twitter bot is running and scheduled to post daily at 7:00 PM.")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
