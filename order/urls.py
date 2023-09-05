from django.urls import path
from .views import upload_order,order_list,edit_order_view
app_name = 'order'
urlpatterns = [
    path('upload/', upload_order, name='order_upload_view'),
    path('list',order_list,name="order_list_view"),
    path('edit/<int:id>/',edit_order_view,name="order_edit_view"),
]