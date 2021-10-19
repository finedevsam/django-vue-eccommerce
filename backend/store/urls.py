from django.urls import path, include
from rest_framework import views
from . views import *


urlpatterns = [
    path('latest-product/', LatestProductsList.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
    path('products/<slug:category_slug>', CategoryDetail.as_view()),
]
