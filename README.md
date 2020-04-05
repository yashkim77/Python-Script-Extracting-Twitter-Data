## Script to Download Twitter Data

Script 'tweetExtracter.py' use to download all the tweets or number of the tweets you want for any Twitter User.

### Setup
* You need to get your Twitter API Credentials by creating a new app at [developer.twitter.com](developer.twitter.com).

* This script uses Tweepy. Install the tweepy package

```
$ sudo pip install tweepy
```

### Clone and use the Python script

```
$ git clone https://github.com/yashkim77/Python-Script-Extracting-Twitter-Data.git
$ cd Python-Script-Extracting-Twitter-Data
```
Enter the consumer_key, consumer_secret, access_key, access_secret in the tweetExtracter.py

Script accept parameter username and number of tweets

```
$ python tweetExtracter.py --username USERNAME --number_of_tweets number
```
If you want to download tweets from more the one twitter handle 
```
$ python tweetExtracter.py --username USERNAME1 USERNAME2 ... --number_of_tweets number
```
If you want to download all the tweets for the twiiter handle
```
$ python tweetExtracter.py --username USERNAME
```
OR
```
$ python tweetExtracter.py --username USERNAME1 USERNAME2 ...
```
