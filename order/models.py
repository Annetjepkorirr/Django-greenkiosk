from django.db import models
from customer.models import Customer
from shopping_cart.models import Shopping_cart
from delivery.models import Delivery


# Create your models here.
class Order(models.Model):
    # shopping_cart=models.ManyToManyField(Shopping_cart)
    order_status  = models.CharField(max_length=10)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.CharField(max_length=32)

    # customer = models.ForeignKey(Customer,null=True,on_delete = models.CASCADE)
    # shopping_cart = models.ForeignKey(shopping_cart,null=True,on_delete=models.CASCADE)
    # delivery = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)
    delivery = models.ManyToManyField(Delivery)