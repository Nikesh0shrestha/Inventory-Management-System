from django import forms
from .models import Product

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'sku',
            'category',
            'price',
            'quantity',
            'supplier',
        ]

        labels = {
            'name': 'Name',
            'sku': 'SKU',
            'category': 'Category',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Laptop',
                    'class': 'form-control'
                }
            ),

            'sku': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. LAAP001',
                    'class': 'form-control'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g. 1020',
                    'class': 'form-control'
                }
            ),

            'quantity': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g. 10',
                    'class': 'form-control'
                }
            ),

            'supplier': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. ABC Corp',
                    'class': 'form-control'
                }
            ),
        }