# kaggle-basic-antiraid

This bot is an example of what can be used to prevent mass spamming and raiding, specifically for kaggle's 
discord server for the event "30 days of Machine Learning" on August 2021.

## Installation:
`$git clone https://github.com/chrisdewa/kaggle-basic-antiraid`
`$cd kaggle-basic-antiraid`
`$python -m pip install -r requirements.txt`

## Additional requirements:
The bot requires a local mongo server running.
It will create or use a database with the name 'kaggle_30dML'
If the bot should connect to a cloud based database edit `config.DATABASE_URL`

## Setup
In `config.py` set the bot's `TOKEN` and adjust any required variables
In the discord server make a "mute role".
Set permissions overwrites in all server's channels so that users with it cannot send messages 
(and any other overwrites desired)

## Running the bot
`python main.py`

## How the bot works:
If any member of the server sends more than 5 messages in 5 seconds, they'll receive 