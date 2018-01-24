from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Appkey


class SignupForm(UserCreationForm):
 
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username',
            }
        )
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password',
            }
        )


class AppkeyForm(ModelForm):

    class Meta:
        model = Appkey
        fields = ['consumer_key', 'consumer_secret', 'access_token', 'access_token_secret']

    def __init__(self, *args, **kwargs):
        super(AppkeyForm, self).__init__(*args, **kwargs)
        self.fields['consumer_key'].widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Consumer Key',
            }
        )
        self.fields['consumer_secret'].widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Consumer Secret',
            }
        )
        self.fields['access_token'].widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Access Token',
            }
        )
        self.fields['access_token_secret'].widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Access Token Secret',
            }
        )
