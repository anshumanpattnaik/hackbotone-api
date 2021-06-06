from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import YoutubeVideo
from .serializers import YoutubeVideoSerializer

# Create your views here.


@method_decorator(name='get', decorator=swagger_auto_schema(tags=['YouTube'], operation_id='Get latest youtube video', operation_description='Returns latest youtube video'))
class GetLatestYoutubeVideo(generics.GenericAPIView):

    serializer_class = YoutubeVideoSerializer

    def get(self, request):
        try:
            youtube_video = YoutubeVideo.objects.get()
            serializer = YoutubeVideoSerializer(youtube_video)
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except YoutubeVideo.DoesNotExist:
            return Response({'error': 'oops! nothing Found'}, status=status.HTTP_404_NOT_FOUND)
