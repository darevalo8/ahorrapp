# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='value_expense',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
