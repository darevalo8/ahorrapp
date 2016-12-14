# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0003_auto_20161213_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
