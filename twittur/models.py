from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class SearchItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200, blank=False)
    is_user_search = models.BooleanField()
    searched_at = models.DateTimeField(auto_now_add=True)

class Tweets(models.Model):
    search_word = models.ForeignKey(SearchItem, on_delete=models.CASCADE)
    data = JSONField()
