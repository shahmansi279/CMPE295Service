# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='NAisle',
            fields=[
                ('aisle_id', models.IntegerField(serialize=False, primary_key=True)),
                ('aisle_num', models.CharField(max_length=45, null=True, blank=True)),
                ('aisle_name', models.CharField(max_length=100, null=True, blank=True)),
                ('aisle_desc', models.CharField(max_length=200, null=True, blank=True)),
                ('aisle_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('aisle_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('aisle_attr3', models.IntegerField(null=True, blank=True)),
                ('aisle_attr4', models.FloatField(null=True, blank=True)),
                ('aisle_attr5', models.DateTimeField(null=True, blank=True)),
                ('aisle_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_AISLE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NAllDeptPdt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_class_id', models.IntegerField()),
                ('product_department', models.CharField(max_length=30, null=True, blank=True)),
                ('product_subcategory', models.CharField(max_length=30, null=True, blank=True)),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=60)),
                ('sku', models.BigIntegerField()),
                ('brand_name', models.CharField(max_length=60, null=True, blank=True)),
                ('prod_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_attr3', models.IntegerField(null=True, blank=True)),
                ('prod_attr4', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_ALL_DEPT_PDT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NAvailProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_class_id', models.IntegerField()),
                ('product_department', models.CharField(max_length=30, null=True, blank=True)),
                ('product_subcategory', models.CharField(max_length=30, null=True, blank=True)),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=60)),
                ('sku', models.BigIntegerField()),
                ('brand_name', models.CharField(max_length=60, null=True, blank=True)),
                ('prod_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_attr3', models.IntegerField(null=True, blank=True)),
                ('prod_attr4', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_AVAIL_PRODUCTS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NOffers',
            fields=[
                ('offer_id', models.IntegerField(serialize=False, primary_key=True)),
                ('offer_start_date', models.DateField(null=True, blank=True)),
                ('offer_end_date', models.DateField(null=True, blank=True)),
                ('offer_creator', models.CharField(max_length=100, null=True, blank=True)),
                ('offer_type', models.CharField(max_length=45, null=True, blank=True)),
                ('offer_desc', models.CharField(max_length=200, null=True, blank=True)),
                ('offer_title', models.CharField(max_length=200, null=True, blank=True)),
                ('offer_img_url', models.ImageField(max_length=500, null=True, upload_to=b'', blank=True)),
                ('offer_img', models.TextField(null=True, blank=True)),
                ('offer_customer_class', models.CharField(max_length=45, null=True, blank=True)),
                ('offer_customer_id', models.IntegerField(null=True, blank=True)),
                ('offer_sensor_id', models.IntegerField(null=True, blank=True)),
                ('offer_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('offer_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('offer_attr3', models.IntegerField(null=True, blank=True)),
                ('offer_attr4', models.FloatField(null=True, blank=True)),
                ('offer_attr5', models.DateTimeField(null=True, blank=True)),
                ('offer_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_OFFERS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NProdStore',
            fields=[
                ('prod_store_id', models.IntegerField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=60, null=True, blank=True)),
                ('product_img_url', models.ImageField(max_length=500, null=True, upload_to=b'', blank=True)),
                ('product_image', models.CharField(max_length=45, null=True, blank=True)),
                ('product_count_available', models.IntegerField(null=True, blank=True)),
                ('prod_store_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_store_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_store_attr3', models.IntegerField(null=True, blank=True)),
                ('prod_store_attr4', models.FloatField(null=True, blank=True)),
                ('prod_store_attr5', models.DateTimeField(null=True, blank=True)),
                ('prod_store_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_PROD_STORE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NProduct',
            fields=[
                ('product_id', models.IntegerField(serialize=False, primary_key=True)),
                ('brand_name', models.CharField(max_length=60, null=True, blank=True)),
                ('product_name', models.CharField(max_length=60)),
                ('sku', models.BigIntegerField(db_column=b'SKU')),
                ('srp', models.DecimalField(null=True, decimal_places=4, max_digits=10, db_column=b'SRP', blank=True)),
                ('gross_weight', models.FloatField(null=True, blank=True)),
                ('net_weight', models.FloatField(null=True, blank=True)),
                ('recyclable_package', models.IntegerField(null=True, blank=True)),
                ('low_fat', models.IntegerField(null=True, blank=True)),
                ('units_per_case', models.SmallIntegerField(null=True, blank=True)),
                ('cases_per_pallet', models.SmallIntegerField(null=True, blank=True)),
                ('shelf_width', models.FloatField(null=True, blank=True)),
                ('shelf_height', models.FloatField(null=True, blank=True)),
                ('shelf_depth', models.FloatField(null=True, blank=True)),
                ('product_img_url', models.ImageField(max_length=500, null=True, upload_to=b'', blank=True)),
                ('product_img', models.TextField(null=True, blank=True)),
                ('product_price', models.FloatField(null=True, blank=True)),
                ('prod_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('prod_attr3', models.IntegerField(null=True, blank=True)),
                ('prod_attr4', models.FloatField(null=True, blank=True)),
                ('prod_attr5', models.DateTimeField(null=True, blank=True)),
                ('prod_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_PRODUCT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NProductClass',
            fields=[
                ('product_class_id', models.IntegerField(serialize=False, primary_key=True)),
                ('product_subcategory', models.CharField(max_length=30, null=True, blank=True)),
                ('product_category', models.CharField(max_length=30, null=True, blank=True)),
                ('product_department', models.CharField(max_length=30, null=True, blank=True)),
                ('product_family', models.CharField(max_length=30, null=True, blank=True)),
                ('prodclass_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('prodclass_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('prodclass_attr3', models.IntegerField(null=True, blank=True)),
                ('prodclass_attr4', models.FloatField(null=True, blank=True)),
                ('prodclass_attr5', models.DateTimeField(null=True, blank=True)),
                ('prodclass_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_PRODUCT_CLASS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NSalesFact1997',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField()),
                ('time_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('promotion_id', models.IntegerField()),
                ('store_id', models.IntegerField()),
                ('store_sales', models.DecimalField(max_digits=10, decimal_places=4)),
                ('store_cost', models.DecimalField(max_digits=10, decimal_places=4)),
                ('unit_sales', models.DecimalField(max_digits=10, decimal_places=4)),
            ],
            options={
                'db_table': 'N_SALES_FACT_1997',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NSensors',
            fields=[
                ('sensor_id', models.IntegerField(serialize=False, primary_key=True)),
                ('sensor_name', models.CharField(max_length=100, null=True, blank=True)),
                ('sensor_desc', models.CharField(max_length=200, null=True, blank=True)),
                ('sensor_battery_level', models.FloatField(null=True, blank=True)),
                ('sensor_status', models.IntegerField(null=True, blank=True)),
                ('sensor_location', models.CharField(max_length=100, null=True, blank=True)),
                ('sensor_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('sensor_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('sensor_attr3', models.IntegerField(null=True, blank=True)),
                ('sensor_attr4', models.FloatField(null=True, blank=True)),
                ('sensor_attr5', models.DateTimeField(null=True, blank=True)),
                ('sensor_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_SENSORS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NStore',
            fields=[
                ('store_id', models.IntegerField(serialize=False, primary_key=True)),
                ('store_name', models.CharField(max_length=200, null=True, blank=True)),
                ('store_desc', models.CharField(max_length=400, null=True, blank=True)),
                ('store_address1', models.CharField(max_length=100, null=True, blank=True)),
                ('store_address2', models.CharField(max_length=100, null=True, blank=True)),
                ('store_city', models.CharField(max_length=45, null=True, blank=True)),
                ('store_state', models.CharField(max_length=45, null=True, blank=True)),
                ('store_zipcode', models.CharField(max_length=25, null=True, blank=True)),
                ('store_phone', models.CharField(max_length=45, null=True, blank=True)),
                ('store_url', models.CharField(max_length=200, null=True, blank=True)),
                ('store_email', models.CharField(max_length=100, null=True, blank=True)),
                ('store_attr1', models.CharField(max_length=1000, null=True, blank=True)),
                ('store_attr2', models.CharField(max_length=1000, null=True, blank=True)),
                ('store_attr3', models.IntegerField(null=True, blank=True)),
                ('store_attr4', models.FloatField(null=True, blank=True)),
                ('store_attr5', models.DateTimeField(null=True, blank=True)),
                ('store_attr6', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'N_STORE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NTimeByDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_id', models.IntegerField()),
                ('the_date', models.DateTimeField(null=True, blank=True)),
                ('the_day', models.CharField(max_length=30, null=True, blank=True)),
                ('the_month', models.CharField(max_length=30, null=True, blank=True)),
                ('the_year', models.SmallIntegerField(null=True, blank=True)),
                ('day_of_month', models.SmallIntegerField(null=True, blank=True)),
                ('week_of_year', models.IntegerField(null=True, blank=True)),
                ('month_of_year', models.SmallIntegerField(null=True, blank=True)),
                ('quarter', models.CharField(max_length=30, null=True, blank=True)),
                ('fiscal_period', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'db_table': 'N_TIME_BY_DAY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NCustomer',
            fields=[
                ('customer', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('account_num', models.BigIntegerField(null=True)),
                ('lname', models.CharField(max_length=30, null=True)),
                ('fname', models.CharField(max_length=30, null=True)),
                ('mi', models.CharField(max_length=30, null=True, blank=True)),
                ('address1', models.CharField(max_length=30, null=True, blank=True)),
                ('address2', models.CharField(max_length=30, null=True, blank=True)),
                ('address3', models.CharField(max_length=30, null=True, blank=True)),
                ('address4', models.CharField(max_length=30, null=True, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('state_province', models.CharField(max_length=30, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('customer_region_id', models.IntegerField(null=True)),
                ('phone1', models.CharField(max_length=30, null=True)),
                ('phone2', models.CharField(max_length=30, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('marital_status', models.CharField(max_length=30, null=True)),
                ('yearly_income', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('total_children', models.SmallIntegerField(null=True)),
                ('num_children_at_home', models.SmallIntegerField(null=True)),
                ('education', models.CharField(max_length=30, null=True)),
                ('date_accnt_opened', models.DateField(null=True)),
                ('member_card', models.CharField(max_length=30, null=True, blank=True)),
                ('occupation', models.CharField(max_length=30, null=True, blank=True)),
                ('houseowner', models.CharField(max_length=30, null=True, blank=True)),
                ('num_cars_owned', models.IntegerField(null=True, blank=True)),
                ('fullname', models.CharField(max_length=60, null=True)),
            ],
            options={
                'db_table': 'N_CUSTOMER',
                'managed': True,
            },
        ),
    ]
