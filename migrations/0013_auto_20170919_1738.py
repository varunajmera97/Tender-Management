# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-19 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendermanagement', '0012_card_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_details',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
    ]