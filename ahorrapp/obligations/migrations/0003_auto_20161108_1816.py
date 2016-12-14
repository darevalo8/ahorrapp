# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0002_auto_20161108_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='end_obligation',
            field=models.DateField(default=datetime.datetime(2016, 11, 8, 23, 16, 57, 11292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='obligation',
            name='name_obligation',
            field=models.CharField(max_length=50),
        ),
    ]
