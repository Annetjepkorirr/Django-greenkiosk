from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product

# Create your views here.
def product_upload_view(request):

   form = ProductUploadForm()
   return render(request,"inventory/product_upload.html",{"form":form})

def products_list(request):
   products = Product.objects.all()
   return render(request, "inventory/products_list.html", {"products":products})   

def products_detail_view(request,id):
   product = Product.objects.get(id = id)
   return render(request, "inventory/product_detail.html", {"product":product})     