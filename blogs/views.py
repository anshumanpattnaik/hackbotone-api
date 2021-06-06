from django.shortcuts import render
from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import Blog
from .serializers import BlogSerializer
from .pagination import Pagination


@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Blogs'], operation_id='Fetch list of blogs', operation_description='Returns list of blogs'))
class FetchBlogsList(generics.ListAPIView):

    queryset = Blog.objects.order_by('-published_date')
    serializer_class = BlogSerializer
    pagination_class = Pagination


@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Blogs'], operation_id='Search blogs', operation_description='Returns list of blogs'))
class SearchBlogs(generics.ListAPIView):

    queryset = Blog.objects.order_by('-published_date')
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'keywords']
    pagination_class = Pagination


@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Blogs'], operation_id='Find Blog by ID', operation_description='Returns a single blog object'))
class FindBlogById(generics.GenericAPIView):

    serializer_class = BlogSerializer

    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(blog_id=blog_id)
            serializer = BlogSerializer(blog)
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK, content_type="text/html")
        except Blog.DoesNotExist:
            return Response({'error': 'oops! nothing Found'}, status=status.HTTP_404_NOT_FOUND)


@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Blogs'], operation_id='List of featured blogs', operation_description='Returns list of featured blogs object'))
class FeaturedBoard(generics.ListAPIView):

    queryset = Blog.objects.filter(featured_board=True)
    serializer_class = BlogSerializer
