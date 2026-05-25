from django.shortcuts import render, redirect

# Create your views here.
from . forms import ProductForm
from . models import Product

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

#UPDATE VIEW

#DELETE VIEW
