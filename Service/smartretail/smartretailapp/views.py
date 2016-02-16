from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from models import NProduct,NProductClass, NAisle, NOffers, NCustomer, NSensors, NStore, NSalesFact1997, NProdStore, NTimeByDay
from serializers import ProductSerializer, CategorySerializer,AisleSerializer,OfferSerializer,CustomerSerializer,SensorSerializer,StoreSerializer,SalesFactSerializer,ProductStoreSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.core import serializers
from django.db import connection
import json

class CategoryList(generics.ListCreateAPIView):

    queryset=NProductClass.objects.all()
    serializer_class=CategorySerializer

    def get_queryset(self):

        category = self.kwargs['category']
        return NProduct.objects.filter(product_class=category)


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
    
    
def login_view(request):

    username = request.GET.get('username','')
    password = request.GET.get('password','')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse(['Logged In'], safe=False)

        else: return JsonResponse(['Error: Disabled Account'], safe=False)
    else: return JsonResponse(['Error: Invalid Credentials'], safe=False)


def logout_view(request):

    logout(request)
    return JsonResponse(['Success'], safe=False)



def register_view(request):

    username = request.GET.get('username','')
    password = request.GET.get('password','')
    first_name = request.GET.get('first_name','')
    last_name = request.GET.get('last_name','')
    email = request.GET.get('email','')
    user_role = request.GET.get('user_role','')
    user_class = request.GET.get('user_class','')
    user_age = request.GET.get('user_age','')
    user_cc_details = request.GET.get('user_cc_details','')
    user_phone = request.GET.get('user_phone','')
    user_addr = request.GET.get('user_addr','')

    user = User.objects.create_user(username, email, password)


    e=NCustomer()
    e.user=user
    e.customer_id=user_role
    e.save()

    return JsonResponse(['Success'], safe=False)


def resetPassword_view(request):

    username = request.GET.get('username','')
    new_password = request.GET.get('new_password','')
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    return JsonResponse(['Password changed'], safe=False)

''' Fetches the distinct category and image for the category '''


def category_list(self):

        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT product_department , prodclass_attr1 FROM G5CMPE295.N_PRODUCT_CLASS")
        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')


def product_list_for_category(self):

        category_name = self.kwargs('category')
        cursor = connection.cursor()
        cursor.execute("SELECT product_class_id  FROM G5CMPE295.N_PRODUCT_CLASS where product_department=%s",category_name)
        data = cursor.fetchall()
        product_data=[]

        for row in data:

            cursor.execute("SELECT product_name, product_id FROM G5CMPE295.N_PRODUCT where product_class_id=%s",row)
            product_data.append(cursor.fetchall())

        return HttpResponse(json.dumps(product_data), content_type='application/json;charset=utf8')




# Create your views here.
