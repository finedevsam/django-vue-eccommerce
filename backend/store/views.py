from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from . models import *
from django.db.models import Q


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
        
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return ({'products': []})