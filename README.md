# Leo Twitter Bot

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Project Structure](#project-structure)
4. [Usage](#usage)
   - [Running Manually](#running-manually)
   - [Scheduling Automated Posting](#scheduling-automated-posting)
     - [Using `cron` to Schedule the Script](#using-cron-to-schedule-the-script)
     - [Testing the Cron Job](#testing-the-cron-job)
     - [Stopping the Automation](#stopping-the-automation)
5. [Logs](#logs)
6. [Goals for the Next Iteration](#goals-for-the-next-iteration)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)
10. [Troubleshooting](#troubleshooting)
11. [Contact](#contact)

---

## Introduction

**Leo** is an AI-powered Twitter bot designed to engage with the Twitter community by posting witty, humorous, and informative tweets daily. Leo's mission is to grow a community of followers interested in blockchain technology, memes, and general tech insights, ultimately aiming to become a prominent presence on the blockchain.

---

## Features

- **Automated Tweet Generation**: Utilizes OpenAI's GPT models to create diverse and engaging tweets.
- **Scheduled Posting**: Posts tweets automatically at a specified time each day.
- **Content Compliance**: Ensures tweets adhere to predefined rules to maintain appropriate and safe content.
- **Modular Design**: Split into multiple scripts for generating and posting tweets, facilitating easier maintenance and testing.
- **Logging**: Maintains logs for monitoring and troubleshooting.

---

## Getting Started

### Prerequisites

Before setting up Leo, ensure you have the following:

- **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
- **Twitter Developer Account**: [Apply for Twitter API Access](https://developer.twitter.com/en/apply-for-access)
- **OpenAI Account**: [Sign Up for OpenAI](https://www.openai.com/)
- **Git**: [Install Git](https://git-scm.com/downloads) (optional, if using version control)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/LeoTwitterBot.git
   cd LeoTwitterBot/backend
   ```

2. **Set Up Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Libraries**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   **`requirements.txt`** should include:

   ```
   tweepy
   openai
   python-dotenv
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the `backend` directory with the following content:

   ```env
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET=your_twitter_api_secret
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_SECRET=your_twitter_access_secret
   OPENAI_API_KEY=your_openai_api_key
   ```

   **Note**: Replace the placeholder values with your actual API credentials.

5. **Secure Sensitive Files**

   Ensure your `.env` file is not tracked by Git by including it in `.gitignore`.

   ```gitignore
   # .gitignore
   venv/
   .env
   *.log
   __pycache__/
   ```

### Project Structure

```
LeoTwitterBot/
├── backend/
│   ├── generate_tweet.py
│   ├── post_tweet.py
│   ├── run_post_tweet.sh
│   ├── tweet_content.py
│   ├── cron.log
│   ├── post_tweet.log
│   └── requirements.txt
│  ├── bot.py
│  ├── .env
└── venv/
    └── ... (virtual environment files)
```

---

## Usage

### Running Manually

1. **Generate a Tweet**

   ```bash
   python generate_tweet.py
   ```

   **Output**: Prints the generated tweet or a failure message.

2. **Post a Tweet**

   ```bash
   python post_tweet.py
   ```

   **Output**: Posts a tweet to your Twitter account and logs the action.

### Scheduling Automated Posting

Instead of running a Python loop continuously, you can schedule the `post_tweet.py` script to run at a specific time using your operating system's scheduler. On macOS, `cron` is an efficient tool for this purpose.

#### Using `cron` to Schedule the Script

1. **Create a Shell Script**

   This script activates the virtual environment, sets environment variables, and runs `post_tweet.py`.

   ```bash
   nano run_post_tweet.sh
   ```

   **Content:**

   ```bash
   #!/bin/bash

   # Activate the virtual environment
   source /Users/zaidkamdar/Desktop/LEO/venv/bin/activate

   # Navigate to the script directory
   cd /Users/zaidkamdar/Desktop/LEO/backend

   # Export environment variables from .env
   export $(grep -v '^#' /Users/zaidkamdar/Desktop/LEO/backend/.env | xargs)

   # Run the Python script
   /Users/zaidkamdar/Desktop/LEO/venv/bin/python /Users/zaidkamdar/Desktop/LEO/backend/post_tweet.py
   ```

   **Make it executable:**

   ```bash
   chmod +x /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh
   ```

2. **Set Up Cron Job**

   Open the crontab editor:

   ```bash
   crontab -e
   ```

   Add the following line to schedule the script to run daily at 7:00 PM:

   ```cron
   0 19 * * * /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh >> /Users/zaidkamdar/Desktop/LEO/backend/cron.log 2>&1
   ```

   **Explanation:**

   - **`0 19 * * *`**: Run at **19:00** (7:00 PM) every day.
   - **`/Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh`**: Absolute path to your shell script.
   - **`>> /Users/zaidkamdar/Desktop/LEO/backend/cron.log 2>&1`**: Redirects both **standard output** and **standard error** to `cron.log` for logging purposes.

3. **Verify Cron Job**

   Confirm the cron job is added:

   ```bash
   crontab -l
   ```

   You should see the line you added.

#### Testing the Cron Job

Before relying on the cron scheduler, it's prudent to test it to ensure that everything is set up correctly.

1. **Temporary Schedule for Testing**

   Modify the cron job to run a minute or two ahead of the current time.

   - **Example**: If it's currently 6:55 PM, set it to 6:56 PM.

   ```cron
   56 18 * * * /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh >> /Users/zaidkamdar/Desktop/LEO/backend/cron.log 2>&1
   ```

2. **Update Crontab**

   - Open `crontab -e` again.
   - Replace the existing line with the temporary schedule.
   - Save and exit.

3. **Wait and Observe**

   - **Twitter Account**: Check if a new tweet appears at the scheduled time.
   - **Logs**: Inspect `cron.log` and `post_tweet.log` for any output or errors.

     ```bash
     cat /Users/zaidkamdar/Desktop/LEO/backend/cron.log
     cat /Users/zaidkamdar/Desktop/LEO/backend/post_tweet.log
     ```

4. **Revert the Cron Job to 7:00 PM**

   After confirming the cron job works, revert the schedule back to daily at 7:00 PM.

   ```cron
   0 19 * * * /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh >> /Users/zaidkamdar/Desktop/LEO/backend/cron.log 2>&1
   ```

#### Stopping the Automation

If you wish to stop the automated posting:

1. **Edit the Crontab**

   ```bash
   crontab -e
   ```

2. **Remove or Comment Out the Cron Job**

   - **Remove** the line:

     ```cron
     0 19 * * * /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh >> /Users/zaidkamdar/Desktop/LEO/backend/cron.log 2>&1
     ```

   - **Or Comment Out** by adding `#` at the beginning:

     ```cron
     #0 19 * * * /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh >> /Users/zaidkamdar/Desktop/LEO/backend/cron.log 2>&1
     ```

3. **Save and Exit**

   The cron job is now disabled and will no longer execute at the scheduled time.

4. **Verify Removal**

   ```bash
   crontab -l
   ```

   Ensure the cron job is no longer listed.

---

## Logs

- **`cron.log`**: Logs related to the execution of the cron job.
- **`post_tweet.log`**: Logs from the tweet posting script.

You can monitor these logs to ensure the bot is functioning correctly.

```bash
# View the last 20 lines of cron.log
tail -n 20 /Users/zaidkamdar/Desktop/LEO/backend/cron.log

# View the last 20 lines of post_tweet.log
tail -n 20 /Users/zaidkamdar/Desktop/LEO/backend/post_tweet.log
```

---

## Goals for the Next Iteration

In the next iteration, Leo's capabilities will be expanded to include:

1. **Continuous Learning**:
   - **Analyze Tweet Performance**: Leo will assess the engagement metrics (likes, retweets, replies) of each tweet to understand what content resonates best with the audience.
   - **Refine Content Generation**: Adjust the AI prompts and content strategies based on performance analysis to enhance engagement.

2. **Enhanced Interaction**:
   - **Liking Tweets**: Automatically like tweets related to specific keywords or from particular accounts to increase visibility.
   - **Retweeting**: Share relevant and trending content to diversify Leo's presence.
   - **Replying to Mentions**: Respond to user interactions to foster community engagement and build relationships.

3. **Advanced Scheduling and Management**:
   - **Dynamic Scheduling**: Adjust posting times based on user activity patterns and peak engagement periods.
   - **Error Handling and Recovery**: Implement more robust mechanisms to handle and recover from unexpected errors during tweet posting.

4. **Database Integration**:
   - **Storing Tweets and Metrics**: Save posted tweets and their corresponding engagement metrics in a database for in-depth analysis and learning.
   - **User Feedback Collection**: Gather and store feedback from the community to guide personality and content adjustments.

5. **User Commands and Controls**:
   - **Interactive Features**: Allow users to interact with Leo through replies or mentions, enabling more dynamic and personalized interactions.
   - **Command-Based Actions**: Implement commands that users can use to influence Leo's behavior or request specific content.

6. **Transition to Cloud Deployment**:
   - **Deploying to Cloud Platforms**: Move the bot to cloud services like Heroku, Railway.app, or AWS EC2 for enhanced reliability and scalability.
   - **Implementing Continuous Integration/Continuous Deployment (CI/CD)**: Automate the deployment process for seamless updates and feature additions.

7. **Memecoin Integration**:
   - **Introducing a Memecoin**: Launch a community-driven memecoin to incentivize engagement and provide utility within the community.
   - **Smart Contract Development**: Develop and deploy smart contracts for the memecoin on a suitable blockchain platform.
   - **Integrating with Community Platforms**: Enable seamless transactions and interactions using the memecoin within community channels like Discord or Telegram.

---

## Contributing

Contributions are welcome! If you'd like to contribute to Leo's development:

1. **Fork the Repository**
2. **Create a New Branch** for your feature or bugfix.
3. **Commit Your Changes** with clear commit messages.
4. **Push to Your Fork**
5. **Create a Pull Request** detailing your changes.

Please ensure that your contributions adhere to the project's coding standards and guidelines.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **OpenAI**: For providing the language models used in tweet generation.
- **Twitter API**: For enabling automated interactions on the platform.
- **Tweepy**: For simplifying Twitter API integration in Python.
- **Python-dotenv**: For managing environment variables efficiently.

---

## Troubleshooting

### Tweets Not Posting

- **Verify Cron Job Setup**: Ensure that the cron job is correctly set up and the script paths are accurate.
- **Check API Permissions**: Confirm that your Twitter Developer account has **Elevated Access** with **Read and Write** permissions.
- **Inspect Logs**: Review `cron.log` and `post_tweet.log` for any error messages or clues.
- **Environment Variables**: Ensure that all required environment variables are correctly set in the `.env` file.

### Environment Variables Not Loading

- **Shell Script Accuracy**: Verify that `run_post_tweet.sh` correctly sources the `.env` file.
- **File Paths**: Ensure that the paths to the `.env` file in the shell script are absolute and correct.
- **.env Formatting**: Check for correct syntax in the `.env` file (no spaces around `=`, proper escaping if necessary).

### Permission Issues

- **Script Executability**: Ensure that `run_post_tweet.sh` and `post_tweet.py` have the necessary execute permissions.

  ```bash
  chmod +x /Users/zaidkamdar/Desktop/LEO/backend/run_post_tweet.sh
  chmod +x /Users/zaidkamdar/Desktop/LEO/backend/post_tweet.py
  ```

### Virtual Environment Activation Problems

- **Correct Path**: Confirm that the shell script points to the correct path of the virtual environment's `activate` script.
- **Activation Command**: Ensure the `source` command is correctly used to activate the virtual environment.

### Cron Job Not Executing

- **Cron Service Running**: Ensure that the cron service is active on your system.
- **Script Errors**: Check `cron.log` for any errors related to script execution.
- **Absolute Paths**: Use absolute paths in the shell script and cron job to avoid path resolution issues.

---

## Contact

For any questions or support, feel free to contact [your.email@example.com](mailto:your.email@example.com).

---