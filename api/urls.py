import os
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="HackbotOne API",
      default_version='v1',
      description="HackbotOne website full api reference",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@hackbotone.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
    re_path('api/v1/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path('api/v1/blogs/', include('blogs.urls'), name='Blogs'),
    re_path('api/v1/portfolio/', include('portfolio.urls'), name='Portfolio'),
    re_path('api/v1/youtube/', include('youtube.urls'), name='YouTube')
]
