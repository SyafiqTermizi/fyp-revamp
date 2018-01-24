from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignupForm, AppkeyForm, SigninForm


def signin(request):
    if request.method == 'POST':
        signin_form = SigninForm(request.POST)

        if signin_form.is_valid():
            usn = signin_form.cleaned_data['username']
            pwd = signin_form.cleaned_data['password']
            user = authenticate(request, username=usn, password=pwd)

            if user is not None:
                login(request, user)
                return redirect('dashboard:index')

            else:
                messages.warning(request, 'Credentials entered are not valid')

    return render(
        request,
        'auth/signin.html',
        {
            'signinform': SigninForm()
        }
    )

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

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('authentication:signin')
