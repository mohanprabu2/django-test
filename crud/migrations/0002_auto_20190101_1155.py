# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-01 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='crud',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]