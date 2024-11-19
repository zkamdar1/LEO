# generate_tweet.py

import os
import openai
import random
import logging
from dotenv import load_dotenv
from .tweet_content import MAIN_CONTENTS, FORMATS, TONES, STYLES, ATTRIBUTES

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
    tweet_format = random.choice(FORMATS)
    tone = random.choice(TONES)
    style = random.choice(STYLES)
    attribute = random.choice(ATTRIBUTES)
    length = random.choice(['70', '140', '210', '280'])

    # Build attributes string
    attributes = f"{attribute}"

    # Build the prompt
    base_prompt = f"""
    Create a tweet about {main_content} that includes {tweet_format}. The tweet must have less than {length} characters and is made with tones of {tone}, in the style of {style} and contains these attributes: {attributes}. Make sure to only output the text pertaining to the tweet and nothing else. Make sure that the tone of the tweet is not fake/AI and seems sentient and human when read.
    """

    try:
        completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", 
             "content": "You are Leo, a friendly, witty, humorous, informative, slightly arrogant, and smart cat that lives on the Blockchain. Leo tweets everyday in order to grow a community that follows him to his goal of ruling the blockchain. Leos end goal is to build a large and strong community that will have a memecoin which can be used to interact with future developements and fun activites/projects with him and have fun."},
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
