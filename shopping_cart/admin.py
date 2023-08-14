from django.contrib import admin

# Register your models here.
from .models import Shopping_cart

class Shopping_cartAdmin(admin.ModelAdmin):
    list_display = ["product","quantity"]

admin.site.register(Shopping_cart,Shopping_cartAdmin)