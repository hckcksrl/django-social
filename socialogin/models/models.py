from django.db import models


class User(models.Model):
    choices = (
        ('kakao', 'kakao'), ('facebook', 'facebook')
    )
    email = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=255, default=None)
    access_token = models.CharField(max_length=255, default=None)
    refresh_token = models.CharField(max_length=255, default=None, null=True, blank=True)
    social_id = models.IntegerField()
    social_site = models.CharField(max_length=255, choices=choices, null=True, blank=True)