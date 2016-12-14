# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='end_obligation',
            field=models.DateField(default=datetime.datetime(2016, 11, 8, 23, 14, 15, 563765, tzinfo=utc)),
        ),
    ]
