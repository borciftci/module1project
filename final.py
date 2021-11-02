from eca import *

from eca.generators import start_offline_tweets

root_content_path = 'static_final'

@event('init')
def setup(ctx, e):
    start_offline_tweets('data/sports_tweets.txt', event_name='chirp', time_factor = 1)

@event('chirp')
def tweet(ctx, e):
    # output for "Current Tweets" and "Most Recent Tweet"
    emit('tweet', e.data)

    # output for "Popular Tweets"
    if e.data['user']['verified'] == True:
        emit('tweetPopular', e.data)