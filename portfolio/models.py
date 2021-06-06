from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    github = models.CharField(max_length=500, blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    linkedin = models.CharField(max_length=500, blank=True)
    youtube = models.CharField(max_length=500, blank=True)
    copyrights = models.CharField(max_length=100, blank=True)
    profile_picture = models.TextField(blank=True)
    short_bio = models.TextField(blank=True)
    promotion_message = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
