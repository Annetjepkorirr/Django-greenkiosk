from rest_framework.views import APIView
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer
from .serializers import OrderSerializer
from order.models import Order
#create various http methods from here

class CustomerListView(APIView):
    def get(self,request):
        customers =Customer.objects.all()
        #data of all customers that are now inJSON format
        serializer = CustomerSerializer(customers, many =True)
        return Response(serializer.data)  #this one is in JSON framework

    def post(self, request):
        serializer = CustomerSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            return  Response(serializer.error, status =HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):
    def get(self, request, id, format= None):
        customer = Customer.object.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, id, format =None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, request.data)
        if serializer.is_valid():
            serializer.solve()
            return Response(serializer.data, status = HTTP_201_CREATED)    
            return Response(serializer.error, status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, id, format =None):
        customer = Customer.objects.get(id = id)
        customer.delete()
        return Response("customer deleted", status = status.HTTP_204_CONTENT)


class OrderListView(APIView):
    def get(self,request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many =True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = OrderSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            return  Response(serializer.error, status =HTTP_400_BAD_REQUEST)

# class Shopping_cartListView(APIView):
#     def get(self,request):
#         shopping_cart = Shopping_cart.objects.all()
#         serializer = Shopping_cartSerializer(order, many =True)
#         return Response(serializer.data) 

#     def post(self, request):
#         serializer = Shopping_cartSerializer(data =request.data)
#         if serializer.is_valid():
#             serializer.save
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#             return  Response(serializer.error, status =HTTP_400_BAD_REQUEST)            

# class AddToCartView(APIView):
#     def post(self,request,format =None):
#         cart_id = request.data["cart_id"]
#         product_id = request.data["product_id"]
#         cart = Shopping_cart.objects.get(id = cart_id)
#         product = Product.objects.get(id = product_id)
#         updated_cart = cart.add_product(product)
#         serializer =  Shopping_cart(updated_cart)
#         return Response(serializer.data)             