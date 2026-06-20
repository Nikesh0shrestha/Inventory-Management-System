from enum import unique
from itertools import product
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.utils.html import MAX_URL_LENGTH
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    descriptions = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField(default=0)
    supplier = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name
    

class StockTransaction(models.Model):
    TRANSACTIONS_TYPES =[('IN','Stock_IN'),('OUT','Stock_Out')]
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="transactions")
    transaction_types = models.CharField(max_length = 10, choices = TRANSACTIONS_TYPES)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null = True,blank = True)

    def __str__(self):
        return f"{self.product_name} - {self.transaction_types}"


    

