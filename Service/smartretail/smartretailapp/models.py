from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.

from django.db import models


class NAisle(models.Model):
    aisle_id = models.IntegerField(primary_key=True)
    aisle_num = models.CharField(max_length=45, blank=True, null=True)
    aisle_name = models.CharField(max_length=100, blank=True, null=True)
    aisle_desc = models.CharField(max_length=200, blank=True, null=True)
    aisle_store = models.ForeignKey('NStore', blank=True, null=True)
    aisle_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    aisle_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    aisle_attr3 = models.IntegerField(blank=True, null=True)
    aisle_attr4 = models.FloatField(blank=True, null=True)
    aisle_attr5 = models.DateTimeField(blank=True, null=True)
    aisle_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_AISLE'


class NAllDeptPdt(models.Model):
    product_class_id = models.IntegerField()
    product_department = models.CharField(max_length=30, blank=True, null=True)
    product_subcategory = models.CharField(max_length=30, blank=True, null=True)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=60)
    sku = models.BigIntegerField()
    brand_name = models.CharField(max_length=60, blank=True, null=True)
    prod_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    prod_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    prod_attr3 = models.IntegerField(blank=True, null=True)
    prod_attr4 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_ALL_DEPT_PDT'


class NAvailProducts(models.Model):
    product_class_id = models.IntegerField()
    product_department = models.CharField(max_length=30, blank=True, null=True)
    product_subcategory = models.CharField(max_length=30, blank=True, null=True)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=60)
    sku = models.BigIntegerField()
    brand_name = models.CharField(max_length=60, blank=True, null=True)
    prod_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    prod_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    prod_attr3 = models.IntegerField(blank=True, null=True)
    prod_attr4 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_AVAIL_PRODUCTS'



class NCustomer(models.Model):

    customer = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)
    account_num = models.BigIntegerField(null=True)
    lname = models.CharField(max_length=30,null=True)
    fname = models.CharField(max_length=30,null=True)
    mi = models.CharField(max_length=30, blank=True, null=True)
    address1 = models.CharField(max_length=30, blank=True, null=True)
    address2 = models.CharField(max_length=30, blank=True, null=True)
    address3 = models.CharField(max_length=30, blank=True, null=True)
    address4 = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state_province = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=30,null=True)
    country = models.CharField(max_length=30,null=True)
    customer_region_id = models.IntegerField(null=True)
    phone1 = models.CharField(max_length=30,null=True)
    phone2 = models.CharField(max_length=30,null=True)
    birthdate = models.DateField(null=True)
    marital_status = models.CharField(max_length=30,null=True)
    yearly_income = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length=30,null=True)
    total_children = models.SmallIntegerField(null=True)
    num_children_at_home = models.SmallIntegerField(null=True)
    education = models.CharField(max_length=30,null=True)
    date_accnt_opened = models.DateField(null=True)
    member_card = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    houseowner = models.CharField(max_length=30, blank=True, null=True)
    num_cars_owned = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=60,null=True)

    class Meta:
        managed = False
        db_table = 'N_CUSTOMER'




class NOffers(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    offer_start_date = models.DateField(blank=True, null=True)
    offer_end_date = models.DateField(blank=True, null=True)
    offer_creator = models.CharField(max_length=100, blank=True, null=True)
    offer_product = models.ForeignKey('NProduct', blank=True, null=True)
    offer_product_class = models.ForeignKey('NProductClass', blank=True, null=True)
    offer_type = models.CharField(max_length=45, blank=True, null=True)
    offer_desc = models.CharField(max_length=200, blank=True, null=True)
    offer_title = models.CharField(max_length=200, blank=True, null=True)
    offer_img_url = models.ImageField(max_length=500, blank=True, null=True)
    offer_img = models.TextField(blank=True, null=True)
    offer_customer_class = models.CharField(max_length=45, blank=True, null=True)
    offer_customer_id = models.IntegerField(blank=True, null=True)
    offer_sensor_id = models.IntegerField(blank=True, null=True)
    offer_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    offer_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    offer_attr3 = models.IntegerField(blank=True, null=True)
    offer_attr4 = models.FloatField(blank=True, null=True)
    offer_attr5 = models.DateTimeField(blank=True, null=True)
    offer_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_OFFERS'





class NProduct(models.Model):
    product_class = models.ForeignKey('NProductClass')
    product_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=60, blank=True, null=True)
    product_name = models.CharField(max_length=60)
    sku = models.BigIntegerField(db_column='SKU')  # Field name made lowercase.
    srp = models.DecimalField(db_column='SRP', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gross_weight = models.FloatField(blank=True, null=True)
    net_weight = models.FloatField(blank=True, null=True)
    recyclable_package = models.IntegerField(blank=True, null=True)
    low_fat = models.IntegerField(blank=True, null=True)
    units_per_case = models.SmallIntegerField(blank=True, null=True)
    cases_per_pallet = models.SmallIntegerField(blank=True, null=True)
    shelf_width = models.FloatField(blank=True, null=True)
    shelf_height = models.FloatField(blank=True, null=True)
    shelf_depth = models.FloatField(blank=True, null=True)
    product_img_url = models.ImageField(max_length=500, blank=True, null=True)
    product_img = models.TextField(blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
    prod_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    prod_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    prod_attr3 = models.IntegerField(blank=True, null=True)
    prod_attr4 = models.FloatField(blank=True, null=True)
    prod_attr5 = models.DateTimeField(blank=True, null=True)
    prod_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_PRODUCT'


class NProductClass(models.Model):
    product_class_id = models.IntegerField(primary_key=True)
    product_subcategory = models.CharField(max_length=30, blank=True, null=True)
    product_category = models.CharField(max_length=30, blank=True, null=True)
    product_department = models.CharField(max_length=30, blank=True, null=True)
    product_family = models.CharField(max_length=30, blank=True, null=True)
    prodclass_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    prodclass_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    prodclass_attr3 = models.IntegerField(blank=True, null=True)
    prodclass_attr4 = models.FloatField(blank=True, null=True)
    prodclass_attr5 = models.DateTimeField(blank=True, null=True)
    prodclass_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_PRODUCT_CLASS'


class NProdStore(models.Model):
    prod_store_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(NProduct, blank=True, null=True)
    product_name = models.CharField(max_length=60, blank=True, null=True)
    product_class = models.ForeignKey(NProductClass, blank=True, null=True)
    product_img_url = models.ImageField(max_length=500, blank=True, null=True)
    product_image = models.CharField(max_length=45, blank=True, null=True)
    product_count_available = models.IntegerField(blank=True, null=True)
    prod_store_aisle = models.ForeignKey(NAisle, blank=True, null=True)
    prod_store_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    prod_store_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    prod_store_attr3 = models.IntegerField(blank=True, null=True)
    prod_store_attr4 = models.FloatField(blank=True, null=True)
    prod_store_attr5 = models.DateTimeField(blank=True, null=True)
    prod_store_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_PROD_STORE'


class NSalesFact1997(models.Model):
    product_id = models.IntegerField()
    time_id = models.IntegerField()
    customer_id = models.IntegerField()
    promotion_id = models.IntegerField()
    store_id = models.IntegerField()
    store_sales = models.DecimalField(max_digits=10, decimal_places=4)
    store_cost = models.DecimalField(max_digits=10, decimal_places=4)
    unit_sales = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'N_SALES_FACT_1997'


class NSensors(models.Model):
    sensor_id = models.IntegerField(primary_key=True)
    sensor_name = models.CharField(max_length=100, blank=True, null=True)
    sensor_desc = models.CharField(max_length=200, blank=True, null=True)
    sensor_battery_level = models.FloatField(blank=True, null=True)
    sensor_status = models.IntegerField(blank=True, null=True)
    sensor_location = models.CharField(max_length=100, blank=True, null=True)
    sensor_aisle = models.ForeignKey(NAisle, blank=True, null=True)
    sensor_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    sensor_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    sensor_attr3 = models.IntegerField(blank=True, null=True)
    sensor_attr4 = models.FloatField(blank=True, null=True)
    sensor_attr5 = models.DateTimeField(blank=True, null=True)
    sensor_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_SENSORS'


class NStore(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=200, blank=True, null=True)
    store_desc = models.CharField(max_length=400, blank=True, null=True)
    store_address1 = models.CharField(max_length=100, blank=True, null=True)
    store_address2 = models.CharField(max_length=100, blank=True, null=True)
    store_city = models.CharField(max_length=45, blank=True, null=True)
    store_state = models.CharField(max_length=45, blank=True, null=True)
    store_zipcode = models.CharField(max_length=25, blank=True, null=True)
    store_phone = models.CharField(max_length=45, blank=True, null=True)
    store_url = models.CharField(max_length=200, blank=True, null=True)
    store_email = models.CharField(max_length=100, blank=True, null=True)
    store_attr1 = models.CharField(max_length=1000, blank=True, null=True)
    store_attr2 = models.CharField(max_length=1000, blank=True, null=True)
    store_attr3 = models.IntegerField(blank=True, null=True)
    store_attr4 = models.FloatField(blank=True, null=True)
    store_attr5 = models.DateTimeField(blank=True, null=True)
    store_attr6 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_STORE'


class NTimeByDay(models.Model):
    time_id = models.IntegerField()
    the_date = models.DateTimeField(blank=True, null=True)
    the_day = models.CharField(max_length=30, blank=True, null=True)
    the_month = models.CharField(max_length=30, blank=True, null=True)
    the_year = models.SmallIntegerField(blank=True, null=True)
    day_of_month = models.SmallIntegerField(blank=True, null=True)
    week_of_year = models.IntegerField(blank=True, null=True)
    month_of_year = models.SmallIntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=30, blank=True, null=True)
    fiscal_period = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_TIME_BY_DAY'
