from django.shortcuts import render, redirect

# Create your views here.
from . forms import ProductForm
from . models import Product

from rest_framework.viewsets import ModelViewSet
from . serializers import ProductSerializer
from .models import Product
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