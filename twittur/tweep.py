import tweepy
import json

from django.contrib.auth.models import User
from authentication.models import Appkey


def keyword_search(request):
    k = Appkey.objects.get(user=request.user.id)
    auth = tweepy.OAuthHandler(k.consumer_key, k.consumer_secret)
    auth.set_access_token(k.access_token, k.access_token_secret)
    api = tweepy.API(auth)
    return True


# auth = tweepy.OAuthHandler("oMfqM2x8CMHUxbrBoLFbs180n", "SjWSufD7aXDGtp8ZGQvb5OL3qkAJW6nJX7FWztH7d85QIfn9ca")
# auth.set_access_token('475820825-HAUYVVI9qJljIPzNqVFwg9y5hhe5DKn3nqeP77tW', 'l43KrHbXgi10tTvQTzpWRTGr33PsANVhmRnxhC7NaVi8U')

# api = tweepy.API(auth)


# search by keyword
# search_result = api.search(q='trump', count=200, tweet_mode='extended')
#
# for search_result_json in search_result:
#     print(json.dumps(search_result_json._json))
#     print('\n\n\n')


# search by user
# search_result = api.user_timeline(screen_name='emmawatson', tweet_mode='extended')

# for search_result_json in search_result:
#     print(json.dumps(search_result_json._json))
#     print('\n\n\n')


# search by tweet id
# search_result = api.get_status(id=919948056459661312, tweet_mode='extended')
# print(json.dumps(search_result._json))
