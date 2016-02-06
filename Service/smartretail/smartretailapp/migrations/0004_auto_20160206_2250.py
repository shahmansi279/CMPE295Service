# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartretailapp', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nproduct',
            options={'managed': False},
        ),
    ]
