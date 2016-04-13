from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import NProduct,NProductClass, NAisle, NListInfo, NListPrd, NCartInfo, NCartPrd, NOffers, NCustomer, NSensors, NStore, NSalesFact1997, NProdStore, NTimeByDay,NAllDeptPdt,NAvailProducts
from serializers import ProductSerializer, CategorySerializer, ListSerializer, ListPrdSerializer, CartSerializer, CartPrdSerializer, AisleSerializer, OfferSerializer, UserSerializer, CustomerSerializer,SensorSerializer,StoreSerializer,SalesFactSerializer,ProductStoreSerializer,AvailDeptSerializer,AvailProductsSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection,IntegrityError
from django.views.decorators.csrf import ensure_csrf_cookie , csrf_protect
import json


import logging
logger = logging.getLogger(__name__)


''' ------Login and Register functions starts----------------------------------------------'''



@ensure_csrf_cookie
def login_view(request):



    username = request.GET.get('username','')
    password = request.GET.get('password','')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'status': 'success','id': user.id, 'username': user.username, 'email': user.email})

        else: return JsonResponse({'status': 'error: disabled account'})
    else: return JsonResponse({'status': 'error: invalid credentials'})


def logout_view(request):

    logout(request)
    return JsonResponse({'status': 'success'})



def register_view(request):

    username = request.GET.get('username','')
    password = request.GET.get('password','')
    email = request.GET.get('email','')
    user_addr = request.GET.get('user_addr','')
    user_zip = request.GET.get('user_zip','')
    user_phone = request.GET.get('user_phone','')
    user_dob = request.GET.get('user_dob','')
    user_gender = request.GET.get('user_gender','')
    user_card = request.GET.get('user_card','')

    try:

        user = User.objects.create_user(username, email, password)
        e=NCustomer()
        e.customer=user
        e.address1 = user_addr
        e.postal_code = user_zip
        e.phone1 = user_phone
        e.birthdate = user_dob
        e.gender = user_gender
        e.account_num = user_card
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
        cursor.execute("SELECT DISTINCT(product_department) FROM G5CMPE295.N_AVAIL_PRODUCTS where prod_attr3 is not null ORDER BY product_department asc ");

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')


def avail_category_for_dept_list(request):

        dept = request.GET.get('dept','')

        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT (product_subcategory) FROM G5CMPE295.N_AVAIL_PRODUCTS where prod_attr3 is not null and (product_department=%s) ORDER BY product_subcategory asc ",[dept]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')



class avail_products_for_category(generics.ListAPIView):

    try:

        logger.debug("Entering store_id conditional block")



        serializer_class = AvailProductsSerializer

        def get_queryset(self):

            subcategory = self.kwargs['subcategory']
            return NAvailProducts.objects.filter(product_subcategory=subcategory).exclude(prod_attr3__isnull=True)


    except Exception, e:

        logger.exception(e)


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





class CartList(APIView):

    def get(self, request, format=None):
        carts = NCartInfo.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartDetail(APIView):

    def get_object(self, pk):
        try:
            return NCartInfo.objects.get(pk=pk)
        except NCartInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart = CartSerializer(cart)
        return Response(cart.data)

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def cart_for_user(request):

    try:

        logger.debug(request)


        cart_customer_id = request.GET.get('cart_customer_id','')
        cursor = connection.cursor()
        cursor.execute("select cart_id from G5CMPE295.N_CART_INFO where cart_customer_id=%s and cart_status='active'",[cart_customer_id]);
        data = cursor.fetchall()

        if cursor.rowcount == 0:

            cursor = connection.cursor()
            cartid = cursor.execute("INSERT INTO G5CMPE295.N_CART_INFO (cart_status, cart_customer_id) VALUES ('active', %s)",[cart_customer_id]);
            return cartid

        else:
            return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')

    except Exception, e:

        logger.exception(e)

class CartPrdList(APIView):

    def get(self, request, format=None):
        carts = NCartPrd.objects.all()
        serializer = CartPrdSerializer(carts, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = CartPrdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartPrdDetail(APIView):

    def get_object(self, pk):
        try:
            return NCartPrd.objects.get(pk=pk)
        except NCartPrd.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart = CartPrdSerializer(cart)
        return Response(cart.data)

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartPrdSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCartDetail(generics.ListCreateAPIView):

    serializer_class=CartPrdSerializer
    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        return NCartPrd.objects.filter(cart_id=cart_id)


class ListList(generics.ListCreateAPIView):

    queryset=NListInfo.objects.all()
    serializer_class=ListSerializer


class ListDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NListInfo.objects.all()
    serializer_class=ListSerializer

class UserListDetail(generics.ListCreateAPIView):

    serializer_class=ListPrdSerializer
    def get_queryset(self):
        list_id = self.kwargs['list_id']
        return NListPrd.objects.filter(list_id=list_id)

def list_for_user(request):

        list_customer_id = request.GET.get('list_customer_id','')
        cursor = connection.cursor()
        cursor.execute("select list_id from G5CMPE295.N_LIST_INFO where list_customer_id=%s",[list_customer_id]);
        data = cursor.fetchall()

        if cursor.rowcount == 0:

            cursor = connection.cursor()
            listid = cursor.execute("INSERT INTO G5CMPE295.N_LIST_INFO (list_customer_id) VALUES (%s)",[list_customer_id]);
            return listid

        else:
            return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')



def sensors_of_interest(request):

        list_id = request.GET.get('list_id','')
        cursor = connection.cursor()
        cursor.execute("select DISTINCT list_prd_attr2 from G5CMPE295.N_LIST_PRD where list_id=%s",[list_id]);
        data = cursor.fetchall()

        sensor_data =[]
        fields = map(lambda x:x[0], cursor.description)
        for row in data:
            cursor.execute("SELECT DISTINCT(aisle_sensor_id) FROM G5CMPE295.N_AISLE where aisle_name=%s",row)
            aisle_data = cursor.fetchall()

            for item in aisle_data:
                cursor.execute("SELECT * FROM G5CMPE295.N_SENSORS where sensor_id=%s",item)
                fields = map(lambda x:x[0], cursor.description)
                #sensor_data.append(cursor.fetchall())
                sensor_data.append([dict(zip(fields,row)) for row in cursor.fetchall()])


        return HttpResponse(json.dumps(sensor_data), content_type='application/json;charset=utf8')

class ListPrdList(APIView):

    def get(self, request, format=None):
        Lists = NListPrd.objects.all()
        serializer = ListPrdSerializer(Lists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListPrdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        List = self.get_object(pk)
        List.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListPrdDetail(APIView):

    def get_object(self, pk):
        try:
            return NListPrd.objects.get(pk=pk)
        except NListPrd.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        List = self.get_object(pk)
        List = ListPrdSerializer(List)
        return Response(List.data)

    def put(self, request, pk, format=None):
        List = self.get_object(pk)
        serializer = ListPrdSerializer(List, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        List = self.get_object(pk)
        List.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OfferList(generics.ListCreateAPIView):

    queryset=NOffers.objects.all()
    serializer_class=OfferSerializer


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=NOffers.objects.all()
    serializer_class=OfferSerializer

class OfferNearByList(generics.ListAPIView):

    serializer_class=OfferSerializer

    def get_queryset(self):
        zipcode = self.kwargs['zipcode']

        return NOffers.objects.filter(offer_attr1=zipcode)


def offer_code(request):

    offercode = request.GET.get('offercode','')

    cursor = connection.cursor()
    cursor.execute("SELECT offer_attr3 FROM G5CMPE295.N_OFFERS WHERE offer_attr2=%s",[offercode]);
    data = cursor.fetchall()
    return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')


class UserList(generics.ListCreateAPIView):

    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserDetail(generics.ListCreateAPIView):

    serializer_class=UserSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)

'''
def account_details(request):

        username = request.GET.get('username','')

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM G5CMPE295.auth_user, G5CMPE295.N_CUSTOMER WHERE G5CMPE295.auth_user.id=G5CMPE295.N_CUSTOMER.customer_id and auth_user.username=%s",[username]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json;charset=utf8')

'''

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

''' Fetches Frequently Purchased Items by the Customer _START_ - Thiagu '''
''' ----------------------------------------------------'''
def cust_freq_purchases_list(request):

        cust = request.GET.get('cust','')

        cursor = connection.cursor()
        cursor.execute("SELECT COALESCE(GROUP_CONCAT(prd_name separator '\n\n'),'')  FROM G5CMPE295.APT_CUST_FREQ_PURCHASES_ALL WHERE cust_id=%s ORDER BY KOUNT desc, prd_name ASC ",[cust]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')

''' Fetches Frequently Purchased Items by the Customer _END_ - Thiagu '''
''' ----------------------------------------------------'''

''' Fetches NEXT IN BASKET for Admin _START_ - Thiagu '''
''' ----------------------------------------------------'''
def next_in_basket_list (request):

        cust = request.GET.get('cust','')
        productName = request.GET.get('product_name', '')

        cursor = connection.cursor()
        cursor.execute("SELECT coalesce(GROUP_CONCAT(PRODUCT_NAME separator '\n\n'),'') FROM G5CMPE295.APV_NEXT_IN_BASKET WHERE customer_id =%s AND product_name != %s  ORDER BY product_name asc ",[cust,productName]);

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')

''' Fetches NEXT IN BASKET for Admin _END_ - Thiagu '''
''' ----------------------------------------------------'''

''' Fetches SHELF SUGGESTIONS for the Admin _START_ - Thiagu '''
''' ----------------------------------------------------'''
def shelf_suggestions_list(request):

        cursor = connection.cursor()
        cursor.execute("SELECT FREQ_GROUPED_ITEMS FROM G5CMPE295.APT_SHELF_SUGGESTIONS ORDER BY CUST_COUNT desc, FREQ_GROUPED_ITEMS asc LIMIT  15");

        data = cursor.fetchall()

        return HttpResponse(json.dumps(data), content_type='application/json;charset=utf8')

''' Fetches SHELF SUGGESTIONS for the Admin _END_ - Thiagu '''
''' ----------------------------------------------------'''








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
