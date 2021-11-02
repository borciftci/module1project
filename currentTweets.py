from eca import *

from eca.generators import start_offline_tweets

root_content_path = 'currentTweets_static'

@event('init')
def setup(ctx, e):
    start_offline_tweets('data/sports_tweets.txt', event_name='chrip', time_factor = 1000)

@event('chrip')
def tweet(ctx, e):
    # generate output
    emit('tweet', e.data)