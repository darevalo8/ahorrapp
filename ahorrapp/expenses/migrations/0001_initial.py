# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name_expense', models.CharField(max_length=50)),
                ('value_expense', models.IntegerField()),
                ('description', models.TextField(max_length=150, blank=True)),
                ('account', models.ForeignKey(to='incomes.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeExpense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='type_expense',
            field=models.ForeignKey(to='expenses.TypeExpense'),
        ),
        migrations.AddField(
            model_name='expense',
            name='user_profile',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
    ]
