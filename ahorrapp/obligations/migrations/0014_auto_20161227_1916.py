# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0013_auto_20161220_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='obligation',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
