from rest_framework import serializers
from customer.models import Customer

# inheriting
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"   
  