from django.shortcuts import render
from .forms import OrderAploadForm
from order.models import Order
def upload_order(request):
    if request.method == 'POST':
        form = OrderAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderAploadForm()
    return render(request, 'order/order_upload.html', {'form': form})
def order_list(request):
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})
def edit_order_view(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderAploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        form = OrderAploadForm(instance=order)
    return render(request, "order/edit_order.html", {"form": form})