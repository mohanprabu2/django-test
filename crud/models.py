# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Crud(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    created_at = models.DateField(default=timezone.now)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
