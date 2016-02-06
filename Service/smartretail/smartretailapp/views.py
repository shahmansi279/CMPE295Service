from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from models import NProduct,NProductClass, NAisle, NOffers, NCustomer, NSensors, NStore, NSalesFact1997, NProdStore, NTimeByDay

from serializers import ProductSerializer, CategorySerializer,AisleSerializer,OfferSerializer,CustomerSerializer,SensorSerializer,StoreSerializer,SalesFactSerializer,ProductStoreSerializer



class CategoryList(generics.ListCreateAPIView):

    queryset=NProductClass.objects.all()
    serializer_class=CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NProductClass.objects.all()
    serializer_class=CategorySerializer

class ProductList(generics.ListCreateAPIView):

    queryset=NProduct.objects.all()
    serializer_class=ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NProduct.objects.all()
    serializer_class=ProductSerializer


class ProductFilter(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):

        category = self.kwargs['category']
        return NProduct.objects.filter(product_class=category)

class SensorList(generics.ListCreateAPIView):

    queryset=NSensors.objects.all()
    serializer_class=SensorSerializer


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NSensors.objects.all()
    serializer_class=SensorSerializer

class AisleList(generics.ListCreateAPIView):

    queryset=NAisle.objects.all()
    serializer_class=AisleSerializer


class AisleDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NAisle.objects.all()
    serializer_class=AisleSerializer

class OfferList(generics.ListCreateAPIView):

    queryset=NOffers.objects.all()
    serializer_class=OfferSerializer


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NOffers.objects.all()
    serializer_class=OfferSerializer

class CustomerList(generics.ListCreateAPIView):

    queryset=NCustomer.objects.all()
    serializer_class=CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NCustomer.objects.all()
    serializer_class=CustomerSerializer

class StoreList(generics.ListCreateAPIView):

    queryset=NStore.objects.all()
    serializer_class=StoreSerializer


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NStore.objects.all()
    serializer_class=StoreSerializer

class SalesFactList(generics.ListCreateAPIView):

    queryset=NSalesFact1997.objects.all()
    serializer_class=SalesFactSerializer


class SalesFactDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NSalesFact1997.objects.all()
    serializer_class=SalesFactSerializer


class ProductStoreList(generics.ListCreateAPIView):

    queryset=NSalesFact1997.objects.all()
    serializer_class=ProductStoreSerializer

class ProductStoreDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NProdStore.objects.all()
    serializer_class=ProductStoreSerializer


def home(request):

    return HttpResponse("Hello World")

# Create your views here.
