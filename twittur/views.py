import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import KeywordForm, UserForm
from .models import SearchItem, Tweets
from . import tweep

# TODO:
# - retain tweets session untill user click back
# - untangle the code

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

            try:
                del request.session['tweets']
            except KeyError:
                pass

            try:
                del request.session['keyword']
            except KeyError:
                pass

            try:
                del request.session['is_user']
            except KeyError:
                pass

            request.session['tweets'] = json_list
            request.session['keyword'] = keyword
            request.session['is_user'] = False

            return render(
                request,
                'twittur/show.html',
                {
                    'result': results,
                    'keyword': keyword,
                }
            )

    return render(
        request,
        'twittur/keyword.html',
        {'keywordForm': KeywordForm()}
    )

@login_required
def search_user(request):
    if request.method == 'POST':
        user_search_form = UserForm(request.POST)

        if user_search_form.is_valid():
            username = user_search_form.cleaned_data['username']
            count = user_search_form.cleaned_data['count']
            results = tweep.user_search(request, username, count)

            json_list = []
            for x in results:
                json_list.append(json.dumps(x._json))

            try:
                del request.session['tweets']
            except KeyError:
                pass

            try:
                del request.session['keyword']
            except KeyError:
                pass

            try:
                del request.session['is_user']
            except KeyError:
                pass

            request.session['tweets'] = json_list
            request.session['keyword'] = username
            request.session['is_user'] = True

            return render(
                request,
                'twittur/show.html',
                {
                    'result': results,
                    'keyword': username,
                }
            )
    return render(
        request,
        'twittur/keyword.html',
        {'keywordForm': UserForm()}
    )

@login_required
def save(request):
    tweets = request.session['tweets']
    keyword = request.session['keyword']
    is_user = request.session['is_user']

    u = User.objects.get(pk=request.user.id)
    s = SearchItem(user=u, keyword=keyword, is_user_search=is_user)
    s.save()
    for x in tweets:
        s.tweets_set.create(data=x, user=request.user.id)

    del request.session['tweets']
    del request.session['keyword']
    del request.session['is_user']

    messages.success(request, 'Data successfuly saved to DB')

    return redirect('dashboard:index')

@login_required
def show_tweets(request, search_id):
    tweets = Tweets.objects.filter(search_word=search_id)

    result = []
    for x in tweets:
        result.append(json.loads(x.data))

    return render(
        request,
        'twittur/show.html',
        {
            'result': result,
            'disabled': 'disabled',
            'style': 'pointer-events: none',
        }
    )
