from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignupForm, AppkeyForm


def signin(request):
    return render(request, 'auth/signin.html')

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        appkey_form = AppkeyForm(request.POST)

        if signup_form.is_valid() and appkey_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            user.appkey.consumer_key = appkey_form.cleaned_data['consumer_key']
            user.appkey.consumer_secret = appkey_form.cleaned_data['consumer_secret']
            user.appkey.access_token = appkey_form.cleaned_data['access_token']
            user.appkey.access_token_secret = appkey_form.cleaned_data['access_token_secret']
            user.save()

            messages.success(request, 'Registration successful!')
            return redirect('authentication:signin')

        else:
            messages.warning(request, 'Form is not valid')

    return render(
        request,
        'auth/signup.html',
        {
            'signupform': SignupForm(),
            'appkeyform': AppkeyForm()
        }
    )
