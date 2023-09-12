from rest_framework import serializers
from customer.models import Customer
from order.models import Order
# from shopping_cart import Shopping_cart

# inheriting
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"   

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"  

# class Shopping_cartSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many =True)
#     class Meta:
#         model = Order
#         fields = "__all__"  

        
        

  