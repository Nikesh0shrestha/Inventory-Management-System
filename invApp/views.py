from itertools import product
from re import search
from django.shortcuts import render, redirect

# Create your views here.
from . forms import ProductForm
from . models import Category, Product, StockTransaction

from rest_framework.viewsets import ModelViewSet
from . serializers import CategorySerializer, ProductSerializer,StockTransactionSerializer
from .models import Product
from rest_framework.response import Response
from django.db import transaction

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# CRUD = CREATE,READ, UPDATE,AND DELETE

#HOME VIEW 
def home_view(request):
    return render(request, 'invApp/home.html')

#CREATE VIEW
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})


#READ VIEW
def product_list_view(request):
    products = Product.objects.all()
    return render (request, 'invApp/product_list.html',{'products':products})


#UPDATE VIEW
def product_update_view(request, product_id):
    product = product.objects.get(product_id = product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return redirect(request, 'invApp/product_form.html',{'form': form})    



#DELETE VIEW
def product_delete_view(request,product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html',{'product': product})


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'name',
        'sku',
        'supplier'
    ]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StockTransactionViewSet(ModelViewSet):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data["product"]
        qty = serializer.validated_data["quantity"]
        t_type = serializer.validated_data["transaction_type"]


        if t_type == "IN":
            product.quantity += qty
        
        elif t_type == "OUT":
            if product.quantity < qty :
                raise Exception("Not enough Stock!!")
            
            product.quantity -= qty
        
        product.save()

        serializer.save(created_by = self.request.user)
