
from rest_framework.views import APIView
from rest_framework.response import Response, Serializer
from rest_framework import status
from.serializers import ProductSerializer
from .models import Product

from django.shortcuts import get_object_or_404


class ProductAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get(self,request,product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(Product)

        return Response(serializer.data)

    def put(self,request, product_id):
        product = get_object_or_404(Product,id=product_id)
        serializer = ProductSerializer(Product,data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,product_id):
        product = get_object_or_404(Product,id=product_id)
        product.DELETE()

        return Response({"message":"Product deleted successfully!!"},
        status=status.HTTP_204_NO_CONTENT)

