from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from models import NProduct,NProductClass, NAisle, NOffers, NCustomer, NSensors, NStore, NSalesFact1997, NProdStore, NTimeByDay,NAllDeptPdt,NAvailProducts
from serializers import ProductSerializer, CategorySerializer,AisleSerializer,OfferSerializer,CustomerSerializer,SensorSerializer,StoreSerializer,SalesFactSerializer,ProductStoreSerializer,AvailDeptSerializer,AvailProductsSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.db import connection,IntegrityError
import json



''' ------Login and Register functions starts----------------------------------------------'''

def login_view(request):

    username = request.GET.get('username','')
    password = request.GET.get('password','')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'status': 'success'})

        else: return JsonResponse({'status': 'error: disabled account'})
    else: return JsonResponse({'status': 'error: invalid credentials'})


def logout_view(request):

    logout(request)
    return JsonResponse({'status': 'success'})



def register_view(request):

    username = request.GET.get('username','')
    password = request.GET.get('password','')
    #first_name = request.GET.get('first_name','')
    #last_name = request.GET.get('last_name','')
    email = request.GET.get('email','')
    user_addr = request.GET.get('user_addr','')
    user_zip = request.GET.get('user_zip','')
    user_phone = request.GET.get('user_phone','')
    user_dob = request.GET.get('user_dob','')
    user_gender = request.GET.get('user_gender','')

    try:

        user = User.objects.create_user(username, email, password)
        e=NCustomer()
        e.customer=user
        #e.fname=first_name
        #e.lname=last_name
        e.address1 = user_addr
        e.postal_code = user_zip
        e.phone1 = user_phone
        e.birthdate = user_dob
        e.gender = user_gender
        e.save()
        return JsonResponse({'status': 'success'})

    except IntegrityError: return JsonResponse({'status': 'error'})


def resetPassword_view(request):

    username = request.GET.get('username','')
    new_password = request.GET.get('new_password','')
    try:
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return JsonResponse({'status': 'success'})
    except User.DoesNotExist: return JsonResponse({'status': 'error'})


''' ------Login and Register functions ends---------------------'''



''' Fetches complete category and product list starts '''

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

''' Fetches complete category  and product list ends'''

''' ----------------------------------------------------'''


''' Fetches available (selected)  department, category and product list starts '''

def avail_dept_list(request):

        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT(product_department) FROM G5CMPE295.N_AVAIL_PRODUCTS where prod_attr3 is not null");

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')


def avail_category_for_dept_list(request):

        dept = request.GET.get('dept','')

        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT (product_subcategory) FROM G5CMPE295.N_AVAIL_PRODUCTS where prod_attr3 is not null and (product_department=%s)",[dept]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')



class avail_products_for_category(generics.ListAPIView):

    serializer_class = AvailProductsSerializer

    def get_queryset(self):

        subcategory = self.kwargs['subcategory']
        return NAvailProducts.objects.filter(product_subcategory=subcategory).exclude(prod_attr3__isnull=True)


''' Fetches available department (selected)  , category and product list ends '''


''' ----------------------------------------------------'''

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



''' ------------------------------------------------------------'''

''' Fetches the distinct category and image for the category '''




'''
def product_list_for_category(request):

        category_name = request.GET.get('category','')


        cursor = connection.cursor()
        cursor.execute("SELECT product_class_id FROM G5CMPE295.N_PRODUCT_CLASS where (product_department=%s)",[category_name])
        data = cursor.fetchall()
        product_data=[]
        for row in data:
            cursor.execute("SELECT product_name, product_id FROM G5CMPE295.N_PRODUCT where product_class_id=%s",row)
            product_data.append(cursor.fetchall())

        return HttpResponse(json.dumps(product_data), content_type='application/json;charset=utf8')


class avail_category_for_dept_list(generics.ListAPIView):

    serializer_class = AvailDeptSerializer

    def get_queryset(self):

        dept = self.kwargs['dept']
        return NAllDeptPdt.objects.filter(product_department=dept,prod_attr3__isnull=False)


class avail_products_for_category(generics.ListAPIView):

    serializer_class = AvailProductsSerializer

    def get_queryset(self):

        subcategory = self.kwargs['subcategory']
        return NAvailProducts.objects.filter(product_subcategory=subcategory,prod_attr3__isnull=False)

def avail_category_for_dept_list(request):

        dept = request.GET.get('dept','')

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM G5CMPE295.N_ALL_DEPT_PDT where prod_attr3 is not null and (product_department=%s)",[dept]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')

def avail_products_for_category(request):

        subcategory = request.GET.get('subcategory','')

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM G5CMPE295.N_AVAIL_PRODUCTS where prod_attr3 is not null and (product_subcategory=%s)",[subcategory]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')




class avail_category_for_dept_list(generics.ListAPIView):

    serializer_class = AvailDeptSerializer

    def get_queryset(self):

        dept = self.kwargs['dept']
        return NAvailProducts.objects.filter(product_department=dept).exclude(prod_attr3__isnull=True)


 url(r'^api/subcategory/(?P<dept>.+)/$', views.avail_category_for_dept_list.as_view()),

'''


# Create your views here.
