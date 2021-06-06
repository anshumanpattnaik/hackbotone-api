from django.db import models

# Create your models here.


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=100, blank=True)
    youtube_link = models.CharField(max_length=500, blank=True)
    embed_link = models.TextField(blank=True)
