# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0004_auto_20161214_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(1, 'Efectivo'), (2, 'Ahorros'), (3, 'Inversiones'), (4, 'Otros')], default=1),
        ),
        migrations.AlterField(
            model_name='account',
            name='saldo_actual',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='income',
            name='valor_ingreso',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
