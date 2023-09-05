from django.urls import path
from .views import CustomerListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name = "customer_list_view"),
    path("customer/<int:id>/", CustomerListView.as_view(), name = "customer_detail"),
]