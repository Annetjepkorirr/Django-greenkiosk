from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    image  = models.ImageField()
    description = models.TextField()
