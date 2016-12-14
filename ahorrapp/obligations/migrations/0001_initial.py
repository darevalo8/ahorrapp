# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('incomes', '0001_initial'),
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obligation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name_obligation', models.TextField(max_length=50)),
                ('value_obligation', models.DecimalField(decimal_places=10, max_digits=19)),
                ('end_obligation', models.DateField(default=datetime.date(2016, 11, 8))),
                ('completed', models.BooleanField(default=False)),
                ('account', models.ForeignKey(to='incomes.Account')),
                ('type_expense', models.ForeignKey(to='expenses.TypeExpense')),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
