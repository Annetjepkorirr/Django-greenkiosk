from django.contrib import admin
from .models import Shopping_cart

# Register your models here.
class Shopping_cart_admin(admin.ModelAdmin):
    list_display = ("name","price","quantity","total_items")
    
admin.site.register(Shopping_cart,Shopping_cart_admin)  
