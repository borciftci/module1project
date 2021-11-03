from eca import *

from eca.generators import start_offline_tweets

root_content_path = 'static_final'
tweet_amount = 0

def getHashtags(text):
    x = text.split("#")

    list1 = []
    list2 = []
    def count(list1, c):
        return list1.count(c)

    i = 1
    while i < len(x):
        y = (x[i].split(" "))
        

        list1.append(y[0])
        z = count(list1, y[0])

        if (y[0], z-1) in list2:
            list2.remove((y[0], z-1))
            list2.append((y[0], z))
        else:
            list2.append((y[0], z))
        
        i += 1
        
    return list2

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

    # Most Popular Hashtags
    for w in getHashtags(e.data['text']):
        emit('hashtag', {
            'action': 'add',
            'value': ('#' + w[0], w[1])
        })