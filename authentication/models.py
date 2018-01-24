from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Appkey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consumer_key = models.CharField(max_length=200, blank=False)
    consumer_secret = models.CharField(max_length=200, blank=False)
    access_token = models.CharField(max_length=200, blank=False)
    access_token_secret = models.CharField(max_length=200, blank=False)


@receiver(post_save, sender=User)
def create_appkey(sender, instance, created, **kwargs):
    if created:
        Appkey.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_appkey(sender, instance, **kwargs):
    instance.appkey.save()
