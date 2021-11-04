from eca import *
import re

from eca.generators import start_offline_tweets

root_content_path = 'static_final'

# stores amount of tweets per second (used in chart)
tweet_amount = 0

def getTerms(text):

    # stores terms to be excluded
    blacklist = ["the","be","to","of","and","a","in","it","for","not","on","with","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know","take","people","into","year","your","good","some","could","them","see","other","than","then","now","look","only","come","its","over","think","also","back","after","use","two","how","our","work","first","well","way","even","new","want","because","any","these","give","day","most","us","are","that","death","had","need","rent","free","low","right","was"]
    
    # terms and appearance variables store the data that was found in the tweet
    terms = []
    appearance = []

    # remove links within text
    tweet_cleaned = re.sub(r"http\S+", "", text)

    # split into single words
    wordList = re.compile(r"\w+(?:'\w+)*|[^\w\s]").findall(tweet_cleaned)
    for v in wordList:
        # check if word is not in blacklist or smaller then 3 characters
        if not str.lower(v) in blacklist and len(v) >= 3:
            # if term already exists in dataset -> increase appearances by one
            if v in terms:
                i = terms.index(v)
                appearance[i] += 1
            # if the term is new -> append a new entry to the lists
            else:
                terms.append(v)
                appearance.append(1)

    # create list of terms and appearances in correct format
    return list( zip(terms, appearance) )

@event('init')
def setup(ctx, e):

    # initializing tweets
    start_offline_tweets('data/sports_tweets.txt', event_name='chirp', time_factor = 1)

    # initializing chart
    ctx.count = 0
    fire('chart_update', {'previous': tweet_amount})

# event for amount of tweets chart
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


    # hook for most recent tweet (True at the end makes sure it checks for an image in the tweet)
    if "media" in e.data['entities']:
        emit('tweetRecent', e.data, True)

    # Most Popular Terms wordcloud
    for t in getTerms(e.data['text']):
        emit('terms', {
            'action': 'add',
            'value': (t[0], t[1])
        })

    # Most Popular Hashtags wordcloud
    for h in e.data['entities']['hashtags']:
        emit('hashtag', {
            'action': 'add',
            'value': ('#' + h['text'], 1)
        })