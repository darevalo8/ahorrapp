# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0007_auto_20170103_0319'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([]),
        ),
    ]
