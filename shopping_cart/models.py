from django.db import models

from inventory.models import Product
# Create your models here.
class Shopping_cart (models.Model):
    products = models.ManyToManyField(Product) 
    product = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()