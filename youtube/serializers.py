from rest_framework import serializers
from .models import YoutubeVideo


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ('title',
                  'youtube_link',
                  'embed_link')
