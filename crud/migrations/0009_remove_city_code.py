# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-01 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_remove_crud_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='code',
        ),
    ]
