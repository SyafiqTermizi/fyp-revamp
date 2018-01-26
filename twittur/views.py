import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import KeywordForm
from . import tweep


@login_required
def search_keyword(request):
    if request.method == 'POST':
        keyword_search_form = KeywordForm(request.POST)

        if keyword_search_form.is_valid():
            keyword = keyword_search_form.cleaned_data['keyword']
            count = keyword_search_form.cleaned_data['count']
            results = tweep.keyword_search(request, keyword, count)

            json_list = []
            for x in results:
                json_list.append(json.dumps(x._json))

            return render(request, 'twittur/show.html', {'result':results})

    return render(
        request,
        'twittur/keyword.html',
        {'keywordForm': KeywordForm()}
    )

def search_user(request):
    return None
