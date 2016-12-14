# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0007_auto_20161108_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='end_obligation',
            field=models.DateField(default=datetime.datetime(2016, 11, 9, 0, 53, 43, 680091, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='obligation',
            name='value_obligation',
            field=models.DecimalField(max_digits=5, decimal_places=3),
        ),
    ]
