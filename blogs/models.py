from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True)
    blog_id = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    seo_thumbnail = models.CharField(max_length=500, blank=True)
    small_thumbnail = models.CharField(max_length=500, blank=True)
    thumbnail = models.CharField(max_length=500, blank=True)
    keywords = ArrayField(models.CharField(max_length=100), blank=True)
    highlights = models.TextField(blank=True)
    description = models.TextField(blank=True)
    visibility = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    featured_board = models.BooleanField(default=False)
    featured = models.TextField(blank=True)

    class Meta:
        ordering = ['-published_date']
