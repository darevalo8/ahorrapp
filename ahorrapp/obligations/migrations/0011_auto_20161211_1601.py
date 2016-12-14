# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0010_auto_20161108_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='end_obligation',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
