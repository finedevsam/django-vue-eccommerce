from django.db.models import fields
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )
        

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )