from django.db import models

# Create your models here.

class Shopping_cart(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_items= models.CharField(max_length=20)
    
    
