from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializers, BrandSerializers, ProductSerializers
import django_filters
class CategoryList(generics.ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializers
     def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Category.objects.filter(title__icontains=name) 
        return queryset

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializers
     lookup_field = "pk"

class BrandList(generics.ListCreateAPIView):
     queryset = Brand.objects.all()
     serializer_class = BrandSerializers

     def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Brand.objects.filter(title__icontains=name) 
        return queryset
     
class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Brand.objects.all()
     serializer_class = BrandSerializers
     lookup_field = "pk"

class ProductList(generics.ListCreateAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializers

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializers
     lookup_field = "pk"