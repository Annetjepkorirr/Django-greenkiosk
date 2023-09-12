from django.db import models
from customer.models import Customer
from shopping_cart.models import Shopping_cart
from delivery.models import Delivery


# Create your models here.
class Order(models.Model):
    order_status  = models.CharField(max_length=10)
    items = models.CharField(max_length=20)
    customer_information  = models.CharField(max_length=15)
    shopping_cart = models.ForeignKey(Shopping_cart,null=True, on_delete=models.CASCADE)
    delivery= models.OneToOneField(Delivery, null=True,on_delete=models.CASCADE)
    