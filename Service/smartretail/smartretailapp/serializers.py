from rest_framework import serializers
from models import NProduct, NProductClass, NAisle, NListInfo, NListPrd, NCartInfo, NCartPrd, NOffers, NCustomer, NSensors, NStore, NSalesFact1997, NProdStore, NTimeByDay, NAvailProducts,NAllDeptPdt
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=NProductClass
        field=('id','product_class_id')


class ProductSerializer(serializers.ModelSerializer):

    category=CategorySerializer

    class Meta:
        model=NProduct

        field=('id','product_id')



class AisleSerializer(serializers.ModelSerializer):

    category=CategorySerializer

    class Meta:
        model=NAisle

        field=('id','aisle_id')


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model=NListInfo

        field=('id','list_id')


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model=NCartInfo

        field=('id','cart_id')



class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model=NOffers

        field=('id','offer_id')


class AvailProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model=NAvailProducts

        field=('product_class_id')


class AvailDeptSerializer(serializers.ModelSerializer):

    class Meta:
        model=NAllDeptPdt

        field=('id','product_class_id')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User

        field=('id', 'username')


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=NCustomer

        field=('id','customer_id')



class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model=NSensors

        field=('id','sensor_id')


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model=NStore

        field=('id','store_id')


class SalesFactSerializer(serializers.ModelSerializer):

    class Meta:
        model=NSalesFact1997

        field=('product_id','time_id','customer_id')



class ProductStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model=NProdStore

        field=('id','prod_store_id')
