# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0009_auto_20170104_2240'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([]),
        ),
    ]
