from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display  = ("order_status","items","customer_information","shopping_cart","delivery")
    
admin.site.register(Order,OrderAdmin) 

# Register your models here.
