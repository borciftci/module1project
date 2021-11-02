from eca import * 

from eca.generators import start_offline_tweets
import datetime
import textwrap

@event('init')
def setup(ctx, e):
    start_offline_tweets('data/sports_tweets.txt', event_name='chirp', time_factor = 1000000000)

@event('chirp')
def tweet(ctx, e):
    # we receive a tweet
    tweet = e.data
    # nicify text
    text = tweet['text']

    # generate output
    emit('tweet', text)  //sus
