# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0002_account_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='saldo_actual',
            field=models.IntegerField(max_length=15),
        ),
    ]
