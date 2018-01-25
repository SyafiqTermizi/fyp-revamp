from django.urls import path

from . import views

app_name = 'twittur'
urlpatterns = [
    path('keyword', views.search_keyword, name='keyword'),
    path('user', views.search_user, name='user'),
]