import tweepy, Tkinter, json
from time import sleep


# twitter account information
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#def tweetAutonomously():
    #newTweet = main()
    #api.update_status(newTweet)
    #print newTweet

# reading timeline and storing the information in a json file.
def process_or_store(tweet):
   print json.dumps(tweet)

# prints the bot's timeline
#for status in tweepy.Cursor(api.home_timeline).items(10):
    #print(status.text)
    #process_or_store(status._json)

# pulling tweets from a specific user and printing
# UPDATE: if no more new tweets, print that
def pullTweets():
    api = tweepy.API(auth)
    # name of user
    name = ""
    # number of tweets to pull
    tweetCount = 20
    results = api.user_timeline(id = name, count = tweetCount)
    # opens the txt file for user, if not already created, it'll create
    # one for the user
    for tweet in results:
        # if the tweet is a retweet, it'll ignore it
        if tweet.text.startswith("RT") == True:
            pass
        else: 
        # print to the screen the last original x tweets from user
            #print tweet.text + '\n'
            # tweets the last x tweets from user
            api.update_status(status = tweet.text)
            #print ("Tweeted" + tweetCount + " to twitter!")
            #f = open(".txt", "w+")
            #f.write(tweet.text)
            #f.close()
username = ""
# getting tweets and appending to array

#def get_tweets(username):
    #api = tweepy.API(auth) 
    #number_of_tweets = 200
    #tweets = api.user_timeline(screen_name = username)
    #tweets_array = []
    #tweets_for_csv = [tweet.text for tweet in tweets]
    #for j in tweets_for_csv:
        #tweets_array.append(j)
    #print tweets_for_csv


# main function contains the method in which the bot
# retweets users based on a search term. 
def retweetFunction():
    # search term, will update to read from a file of tweets
    search = ""
    if search == "":
        print "Error, try again. There needs to be a search term entered."
    else: 
        numberofTweets = "10"
        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.retweet()
                print("Retweeted this tweet")
        # when tweepy runs into an error, such as trying to retweet
        # something that's already been retweeted, it prints
        # the error message
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

# runs the retweet function
retweetFunction()

# runs the pull function
pullTweets()
