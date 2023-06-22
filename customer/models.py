from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=7)
    second_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=7)
    email = models.EmailField()
    
    
    
