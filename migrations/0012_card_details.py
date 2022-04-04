# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-18 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendermanagement', '0011_auto_20170918_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('card_owner', models.CharField(max_length=50)),
                ('card_number', models.BigIntegerField()),
                ('exp_month', models.CharField(max_length=50)),
                ('exp_year', models.IntegerField()),
            ],
        ),
    ]