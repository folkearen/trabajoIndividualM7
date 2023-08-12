from django.shortcuts import render, redirect

def home(request):
    return render(request, 'task/home.html', {})

def task(request):
    return render(request, 'task/task.html', {})