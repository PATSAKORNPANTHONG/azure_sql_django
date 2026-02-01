from django.shortcuts import render
from .serializers import ProductSerializer, StoreSerializer, UserSerializer
from .models import Product, Store, User
from rest_framework import generics, response, status

# Create your views here.


class StoreList(generics.ListCreateAPIView): #GET/POST
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView): #DELETE
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'


class StoreDeleteAll(generics.DestroyAPIView): #DELETE all
    def delete(self, request, *args, **kwargs):
        # Delete all Store objects
        Store.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
#############################################
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'

class UserDeleteAll(generics.DestroyAPIView): #DELETE all
    def delete(self, request, *args, **kwargs):
        # Delete all User objects
        User.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)