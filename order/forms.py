from django import forms
from .models import Order
class OrderAploadForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'