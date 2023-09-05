from rest_framework.views import APIView
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer
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


