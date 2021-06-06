from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import Portfolio
from .serializers import PortfolioSerializer

# Create your views here.

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Portfolio'], operation_id='Get user portfolio', operation_description='Returns user portfolio'))
class GetPortfolio(generics.GenericAPIView):

    serializer_class = PortfolioSerializer

    def get(self, request):
        try:
            portfolio = Portfolio.objects.get()
            serializer = PortfolioSerializer(portfolio)
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Portfolio.DoesNotExist:
            return Response({'error': 'oops! nothing Found'}, status=status.HTTP_404_NOT_FOUND)
