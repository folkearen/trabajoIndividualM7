from django.forms import ModelForm
from django import forms
from ...models import Task

class CreateTask(ModelForm):
    class Meta:
        model = Task
        exclude = ['task_owner', 'status']
        labels = {
            'title' : 'Título',
            'description' : 'Descripción',
            'deadline' : 'Fecha límite',
            'status' : 'Estado',

            
        }
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }

class EditTask(ModelForm):
    class Meta:
        model = Task
        exclude = ['task_owner']