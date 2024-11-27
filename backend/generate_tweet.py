# generate_tweet.py

import os
import openai
import random
import logging
from dotenv import load_dotenv
from .tweet_content import MAIN_CONTENTS, TONES, ATTRIBUTES

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='generate_tweet.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# OpenAI Authentication
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY


def generate_tweet():
    """
    Generates a tweet using OpenAI's API based on random selections from content lists.
    """
    main_content = random.choice(MAIN_CONTENTS)
    tone = random.choice(TONES)
    attribute = random.choice(ATTRIBUTES)
    length = random.choice(['70', '140', '210', '280'])

    # Build attributes string
    attributes = f"{attribute}"

    # Build the prompt
    base_prompt = f"""
    Create a tweet about {main_content}. The tweet must have less than {length} characters and is made with tones of {tone} and contains these attributes: {attributes}. Make sure to only output the text pertaining to the tweet and nothing else. 
    """

    try:
        completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", 
             "content": "You are Leo an informative, slightly arrogant, and smart cat that lives online. You want to help people and grow a positive and fostering community through your tweets and the contents in them. Leos end goal is to build a large and strong community that are willing to learn, grind, work hard, help others, be moral, and make money. Make sure that the tone of the tweet is not cringey and instead is actionable, concise, and human."},
            {
                "role": "user",
                "content": base_prompt
            }
        ]
        )

        tweet = completion.choices[0].message.content

        return tweet

    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return None

if __name__ == "__main__":
    tweet = generate_tweet()
    if tweet:
        print(f"Generated Tweet:\n{tweet}")
        print(len(tweet))
    else:
        print("Failed to generate a valid tweet.")
