from django.urls import path
from .views import product_upload_view
from .views import products_list
from .views import products_detail_view


urlpatterns = [
    path("products/upload/",product_upload_view,name="product_upload_views"),
    path("products/list/", products_list, name = "products_list"),
    path("products/<int:id>/", products_detail_view, name = "product_detail")
]