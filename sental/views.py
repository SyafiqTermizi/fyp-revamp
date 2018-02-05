from django.shortcuts import render
from twittur.models import SearchItem, Tweets
from django.http import HttpResponse

def index(request):
    saved_searched = SearchItem.objects.filter(user=request.user.id)
    return render(request, 'sental/index.html', {'saved_search':saved_searched})
