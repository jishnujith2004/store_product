from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from store_project.serializers import ProductSerializer,UserSerializer
from store_project.models import Product

# Create your views here.
class UserSign(CreateAPIView):
    serializer_class=UserSerializer

class CreateProduct(CreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()


class ListAllProduct(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
