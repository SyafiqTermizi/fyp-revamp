from django.urls import path

from . import views

app_name = 'sental'
urlpatterns = [
    path('', views.index, name='index'),
]
