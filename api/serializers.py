from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializers(serializers.ModelSerializer):
     class Meta:
          model = Category
          fields = ('id', 'title', 'slug')

class BrandSerializers(serializers.ModelSerializer):
     class Meta:
          model = Brand
          fields = ('id', 'title')

class ProductSerializers(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = ('__all__')