from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from . models import *



"""Create User/ User Management"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    username = request.data.get('userName')
    fullname = request.data.get('fullname')
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    is_admin = request.data.get('isAdmin')
    
    """Check the user that is creating the User"""
    if request.user.is_superuser == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Permission Denied"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        if password == confirm_password:
            """Create User"""
            if is_admin == bool(True):
                user = User.objects.create_user(username=username, fullname=fullname, email=email, password=password, is_superuser=True)
                user.save()
                data = {
                    "code": status.HTTP_200_OK,
                    "status": "successful",
                    "message": "User Created"
                }
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                user = User.objects.create_user(username=username, fullname=fullname, email=email, password=password, is_customer=True)
                user.save()
                data = {
                    "code": status.HTTP_200_OK,
                    "status": "successful",
                    "message": "User Created"
                }
                return Response(data=data, status=status.HTTP_200_OK)
            
        
        else:
            data = {
                "code": status.HTTP_401_UNAUTHORIZED,
                "status": "fail",
                "message": "Password not match"
            }
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
        
        


"""Create Product"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    prod_title = request.data.get('productTitle')
    prod_desc = request.data.get('productDesc')
    prod_cat = request.data.get('productCategory')
    price = request.data.get('price')
    qty = request.data.get('quantity')
    
    if request.user.is_superuser == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Permission Denied"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    else:
        try:
            cat = get_object_or_404(Category, id=prod_cat)
            
            """Create Product"""
            prod = Product(prod_title=prod_title, prod_desc=prod_desc, cat_id=cat.id, price=price, qty=qty)
            prod.save()
            
            data = {
                    "code": status.HTTP_200_OK,
                    "status": "successful",
                    "message": "Product Created"
                }
            return Response(data=data, status=status.HTTP_200_OK)
            
        except:
            data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Invalid Category ID"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    

"""Delete Product"""
@api_view(['DELETE'])
@permission_classes(IsAuthenticated)
def delete_product(request, id):
    if request.user.is_superuser == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Permission Denied"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
    elif Product.objects.filter(id=id).exists() == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Invalid Product ID"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
        
        instance = Product.objects.filter(id=id)
        instance.delete()
        
        data = {
            "code": status.HTTP_200_OK,
            "status": "successful",
            "message": "Product Remove"
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
    

"""Delete Product"""
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, id):
    prod_title = request.data.get('productTitle')
    prod_desc = request.data.get('productDesc')
    prod_cat = request.data.get('productCategory')
    price = request.data.get('price')
    qty = request.data.get('quantity')
    if request.user.is_superuser == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Permission Denied"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
    elif Product.objects.filter(id=id).exists() == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Invalid Product ID"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
        try:
            cat = get_object_or_404(Category, id=prod_cat)
        
            instance = Product.objects.filter(id=id)
            instance.update(prod_title=prod_title, prod_desc=prod_desc, cat_id=cat.id, price=price, qty=qty)
        
            data = {
                "code": status.HTTP_200_OK,
                "status": "successful",
                "message": "Product Updated"
            }
            return Response(data=data, status=status.HTTP_200_OK)
        
        except:
            data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Invalid Category ID"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
    


"""create Category"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    name = request.data.get('name')
    if request.user.is_superuser == False:
        data = {
            "code": status.HTTP_401_UNAUTHORIZED,
            "status": "fail",
            "message": "Permission Denied"
        }
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
        cat = Category(name=name)
        cat.save()
        data = {
            "code": status.HTTP_200_OK,
            "status": "successful",
            "message": "Category Created"
        }
        return Response(data=data, status=status.HTTP_200_OK)
    

"""Get all Category"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_category(request):
    snippet = Category.objects.filter()
    serialize = CategorySerializer(instance=snippet, many=True)
    return Response(data=serialize.data, status=status.HTTP_200_OK)



"""all Product"""
@api_view(['GET'])
@permission_classes([])
def allproduct(request):
    snippet = Product.objects.filter()
    
    serialize = ProductSerializer(instance=snippet, many=True)
    return Response(data=serialize.data, status=status.HTTP_200_OK)



"""Product by Cat"""
@api_view(['GET'])
@permission_classes([])
def prodbyid(request, catid):
    snippet = Product.objects.filter(cat_id=catid)
    
    serialize = ProductSerializer(instance=snippet, many=True)
    return Response(data=serialize.data, status=status.HTTP_200_OK)
    
        
    