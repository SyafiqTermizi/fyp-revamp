from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from twittur.models import SearchItem, Tweets


@login_required
def index(request):
    recent_search = SearchItem.objects.filter(user=request.user.id)[:5]
    saved_tweets = Tweets.objects.filter(user=request.user.id).count()
    searched_user = SearchItem.objects.filter(user=request.user.id, is_user_search=True).count()
    searched_keyword = SearchItem.objects.filter(user=request.user.id, is_user_search=False).count()
    context = {
        'recent_search': recent_search,
        'saved_tweets': saved_tweets,
        'searched_user': searched_user,
        'searched_keyword': searched_keyword,
    }
    return render(request, 'dashboard/index.html', context)
