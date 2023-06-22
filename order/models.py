from django.db import models


# Create your models here.
class Order(models.Model):
    order_status  = models.CharField(max_length=10)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.CharField(max_length=32)
