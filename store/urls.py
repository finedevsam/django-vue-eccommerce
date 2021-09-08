from django.urls import path, include
from rest_framework import views
from . import views


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('create_user/', views.create_user, name='create_user'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/<str:id>', views.delete_product, name='delete_product'),
    path('update_product/<str:id>', views.update_product, name='update_product'),
    path('create_category/', views.create_category, name='create_category'),
    path('all_category/', views.all_category, name='all_category'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('prodbyid/<str:catid>', views.prodbyid, name='prodbyid'),
    
]
