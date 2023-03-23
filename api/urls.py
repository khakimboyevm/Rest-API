from django.urls import path
from .views import *

urlpatterns = [
     path('categories/', CategoryList.as_view()),
     path('brands/', BrandList.as_view()),
     path('categories/<int:pk>/', CategoryDetail.as_view()),
     path('brands/<int:pk>/', BrandDetail.as_view()),
     path('products/', ProductList.as_view()),
     path('products/<int:pk>/', ProductDetail.as_view()),
]