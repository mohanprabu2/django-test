# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    args = {'user':request.user}
    return render(request, 'crud/crud_home.html', args)
