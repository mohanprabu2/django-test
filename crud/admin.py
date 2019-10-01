# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Crud, City

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

class CrudAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'created_at', 'city', 'is_active']
    ordering = ['name', 'age', 'created_at']
    list_filter  = ['age']
    list_editable = ['age', 'is_active']
    search_fields = ['name', 'age', 'city__name']
    date_hierarchy = 'created_at'
    fields = [('name', 'age'), 'city', 'is_active']

admin.site.register(Crud, CrudAdmin)
admin.site.register(City, CityAdmin)