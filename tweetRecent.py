from eca import *

from eca.generators import start_offline_tweets

root_content_path = 'static_tweetRecent'

@event('init')
def setup(ctx, e):
    start_offline_tweets('data/sports_tweets.txt', event_name='chirp', time_factor = 1)

@event('chirp')
def tweet(ctx, e):
    # generate output
    emit('tweet', e.data)