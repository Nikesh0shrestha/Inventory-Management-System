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

        model = Category

        fields = '__all__'

class StockTransactionSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(sourse="product_name",ready_only = True)   

    class Meta:

        model = StockTransaction

        fields = [
            "id",
            "product",
            "product_name",
            "transaction_type",
            "quantity",
            "created_by",
            "created_at",
        ]

        read_only_fields = [
            "created_by",
            "created_at",
        ]