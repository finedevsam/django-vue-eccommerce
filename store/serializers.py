from django.db.models import fields
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
from .models import *


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        fields = "__all__"