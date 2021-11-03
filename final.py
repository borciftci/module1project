from eca import *

from eca.generators import start_offline_tweets

root_content_path = 'static_final'
tweet_amount = 0

@event('init')
def setup(ctx, e):

    # initializing tweets
    start_offline_tweets('data/sports_tweets.txt', event_name='chirp', time_factor = 1)

    # initializing graph
    ctx.count = 0
    fire('chart_update', {'previous': tweet_amount})

@event('chart_update')
def chart(ctx, e):
    ctx.count += 1

    global tweet_amount

    # get current amount of tweets and reset counter
    sample = tweet_amount
    tweet_amount = 0

    # emit sample to graph
    emit('chart_value', {
        'action': 'add',
        'value': sample
    })

    fire('chart_update', {'previous': sample}, delay=1)


@event('chirp')
def tweet(ctx, e):

    # add to tweet amount counter
    global tweet_amount
    tweet_amount += 1

    # output for "Current Tweets" and "Most Recent Tweet"
    emit('tweet', e.data)

    # output for "Popular Tweets"
    if e.data['user']['verified'] == True:
        emit('tweetPopular', e.data)


    # e.data['entities']['media'][0]['media_url']
    if "media" in e.data['entities']:
        emit('tweetRecent', e.data, True)