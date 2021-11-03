from eca import * 

from eca.generators import start_offline_tweets

list_tweets = []
temp1 = []


# root_content_path = 'test1_static'

@event('init')
def setup(ctx, e):
    start_offline_tweets('data/sports_tweets.txt', event_name='chirp', 
            time_factor = 100000)

@event('chirp')
def tweet(ctx, e):
    x = e.data

    list_tweets.append([x, (x["quote_count"] + x["reply_count"] + x["retweet_count"] + x["favorite_count"])])
    for i in range(len(list_tweets)):
        print(list_tweets[i][1])

    #emit('tweet', e.data)
