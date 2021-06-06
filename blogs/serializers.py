from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'blog_id', 'author', 'published_date', 'last_updated_date', 'seo_thumbnail', 'small_thumbnail', 'thumbnail',
                  'keywords', 'highlights', 'description', 'visibility',
                  'is_featured', 'featured_board', 'featured']
