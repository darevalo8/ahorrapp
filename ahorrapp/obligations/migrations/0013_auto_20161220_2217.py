# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0012_auto_20161220_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='value_obligation',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
