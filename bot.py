# bot.py
import logging
from backend.post_tweet import post_tweet

# Configure logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def main():
    post_tweet()

if __name__ == "__main__":
    main()
