# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-10 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendermanagement', '0007_auto_20170908_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_request',
            name='category',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='t_request',
            name='t_type',
            field=models.IntegerField(),
        ),
    ]
