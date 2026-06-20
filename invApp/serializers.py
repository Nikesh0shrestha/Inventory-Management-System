from dataclasses import fields
from unicodedata import category
from rest_framework import serializers
from .models import Product,Category,StockTransaction


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product

        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:

        model = category

        fields = '__all__'

class StockTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = StockTransaction

        fields = "__all__"