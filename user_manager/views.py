from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import forms
# Create your views here.

def logout(request):
    logout(request)

def register(request):
    return render(request, 'registration/register.html', {
        'form' : forms.CustomCreationForm()
    })

