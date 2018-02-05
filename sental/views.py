from django.shortcuts import render
from twittur.models import SearchItem, Tweets
from twittur.models import Tweets

from . import classify

def index(request):
    saved_searched = SearchItem.objects.filter(user=request.user.id)
    return render(request, 'sental/index.html', {'saved_search':saved_searched})

def analyse(request, search_id):
    tweets = Tweets.objects.filter(search_word=search_id)
    sental = classify.analyse(tweets)

    neg = 0
    pos = 0
    neut = 0
    for x in sental:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            neut += 1

    context = {
        'neg': neg,
        'pos': pos,
        'neut': neut,
    }
    return render(request, 'sental/analyse.html', context=context)