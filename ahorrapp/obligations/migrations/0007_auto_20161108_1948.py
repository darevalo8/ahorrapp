# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0006_auto_20161108_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='end_obligation',
            field=models.DateField(default=datetime.datetime(2016, 11, 9, 0, 48, 53, 763118, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='obligation',
            name='value_obligation',
            field=models.DecimalField(max_digits=4, decimal_places=3),
        ),
    ]
