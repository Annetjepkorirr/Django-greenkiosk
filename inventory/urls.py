from django.urls import path
from .views import product_upload_view
from .views import products_list
from .views import product_detail
from .views import product_update_view
from .views import delete_product


urlpatterns = [
    path("products/upload/",product_upload_view,name="product_upload_views"),
    path("products/list/", products_list, name = "products_list"),
    path("products/<int:id>/", product_detail, name="product_detail_view"),
    path('inventory/products/edit/<int:id>/', product_update_view, name='product_update'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),


]