# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0005_auto_20161220_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
