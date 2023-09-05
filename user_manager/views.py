from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import forms
# Create your views here.
@login_required
def logout(request):
    logout(request)

def register(request):
    if request.method == 'POST':
        formulario_post = forms.CustomCreationForm(request.POST)
        if formulario_post.is_valid():
            user = formulario_post.save()
            login(request,user)
            return redirect('task')
        else:
            return render(request, 'registration/register.html', {
                'form' :  forms.CustomCreationForm(),
                'errors' : formulario_post.errors
            })
            
    return render(request, 'registration/register.html', {
        'form' : forms.CustomCreationForm()
    })

