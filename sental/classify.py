import json

from textblob import TextBlob


def analyse(tweet_object):
    sentiment = []
    for item in tweet_object:
        sentence = TextBlob(json.loads(item.data)['full_text'])
        sentiment.append(sentence.sentiment.polarity)

    return sentiment

# X.append(json.loads(item.data)['full_text'])
