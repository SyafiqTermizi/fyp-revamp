from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import tweep

@login_required
def search_keyword(request):
    if tweep.keyword_search(request):
        return HttpResponse(request.user.id)
    return HttpResponse('tak jadi')

def search_user(request):
    return None
