from rest_framework import serializers
from .models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name',
                  'facebook',
                  'github',
                  'twitter',
                  'linkedin',
                  'youtube',
                  'copyrights',
                  'profile_picture',
                  'short_bio',
                  'promotion_message',
                  'about_me')
