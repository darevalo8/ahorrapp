# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20161220_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
