# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name_account', models.CharField(max_length=50)),
                ('saldo_actual', models.IntegerField()),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre_ingreso', models.CharField(max_length=50)),
                ('valor_ingreso', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=300)),
                ('account', models.ForeignKey(to='incomes.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeIncome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='type_income',
            field=models.ForeignKey(to='incomes.TypeIncome'),
        ),
        migrations.AddField(
            model_name='income',
            name='user_profile',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
    ]
