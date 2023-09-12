from django.urls import path
from .views import CustomerListView
from .views import OrderListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name = "customer_list_view"),
    path("customer/<int:id>/", CustomerListView.as_view(), name = "customer_detail"),
    path("order/", OrderListView.as_view(), name = "order_list_view"),
    path("order/<int:id>/", OrderListView.as_view(), name = "order_detail"),
    # path("shopping_cart/", Shopping_cartListView.as_view(), name = "shopping_cart_list_view"),
    # path("shopping_cart/<int:id>/", Shopping_cartListView.as_view(), name = "order_detail"),
    # path("add_to_cart/",AddToCartView.as_view(), name ="add_to_cart")
]
