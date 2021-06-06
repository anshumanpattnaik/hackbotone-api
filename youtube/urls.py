import os
from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('latest', GetLatestYoutubeVideo.as_view())
]