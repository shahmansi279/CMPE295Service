# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smartretailapp', '0002_auto_20160205_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_role', models.CharField(max_length=200)),
                ('user_class', models.CharField(max_length=200)),
                ('user_age', models.CharField(max_length=100)),
                ('user_cc_details', models.CharField(max_length=200)),
                ('user_phone', models.CharField(max_length=100)),
                ('user_addr', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
