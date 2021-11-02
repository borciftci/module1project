import json

# 'quote_count': 0, 'reply_count': 0, 'retweet_count': 0, 'favorite_count': 0

file1 = open('data/sports_tweets_test.txt')

readfile = file1.readlines()


converted = []
for i in readfile:
    converted.append(json.loads(i))

temp1 = []
for i in converted:
    temp1.append([i, (i['quote_count'] + i['reply_count'] + i['retweet_count'] + i['favorite_count'])])


for i in range(len(temp1)):
    print(temp1[i][1])
    




