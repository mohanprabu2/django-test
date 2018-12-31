# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def home(request):
    name = 'Mohan'
    args = {'name':name}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
        else:
            args = {'form': form}
            return render(request, 'accounts/register.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)

@login_required
def profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')