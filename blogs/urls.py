import os
from django.urls import re_path, path
from .views import *

urlpatterns = [
    re_path('list', FetchBlogsList.as_view()),
    re_path('search', SearchBlogs.as_view()),
    path('<str:blog_id>/', FindBlogById.as_view()),
    path('featured-board', FeaturedBoard.as_view())
]