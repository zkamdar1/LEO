# bot.py
import schedule
import time
import logging
from backend.post_tweet import post_tweet

# Configure logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def main():
    # Schedule the bot to post every day at 7:00 PM
    schedule.every().day.at("13:00").do(post_tweet)

    logging.info("Leo bot started. Scheduled to post daily at 1:00 PM.")
    print("Leo bot is running and scheduled to post daily at 1:00 PM.")

    schedule.every().day.at("20:30").do(post_tweet)

    logging.info("Leo bot started. Scheduled to post daily at 8:30 PM.")
    print("Leo bot is running and scheduled to post daily at 8:30 PM.")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
