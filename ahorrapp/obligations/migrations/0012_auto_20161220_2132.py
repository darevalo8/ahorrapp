# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligations', '0011_auto_20161211_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obligation',
            name='type_expense',
        ),
        migrations.AddField(
            model_name='obligation',
            name='type_obligation',
            field=models.IntegerField(choices=[(1, 'Educacion'), (2, 'Hogar'), (3, 'Creditos'), (4, 'Otros')], default=4),
        ),
    ]
