# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(default=1, choices=[(1, 'Dinero'), (2, 'Ahorros'), (3, 'Inversiones'), (4, 'Salario'), (5, 'Otros')]),
        ),
    ]
