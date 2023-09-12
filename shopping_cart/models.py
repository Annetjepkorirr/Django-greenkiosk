from django.db import models

from inventory.models import Product
# Create your models here.
class Shopping_cart (models.Model):
    # products = models.ManyToManyField(Product) 
    product = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField()

    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self

    def get_total(self):
        products =self.products
        total = 0
        for product in products:
            total += product.price
        return total   
