# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-01 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20190101_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='city',
            field=models.ManyToManyField(to='crud.City'),
        ),
    ]