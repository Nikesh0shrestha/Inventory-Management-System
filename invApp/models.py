from enum import unique
from django.db import models
from django.utils.html import MAX_URL_LENGTH

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50,unique=True)
    price  = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    


class Category(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    descriptions = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

