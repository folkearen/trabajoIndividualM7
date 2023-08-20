from django.forms import ModelForm
from django import forms
from django.utils import timezone
from ...models import Task
from datetime import date

class CreateTask(ModelForm):
    class Meta:
        model = Task
        exclude = ['task_owner', 'status']
        labels = {
            'title' : 'Título',
            'description' : 'Descripción y observaciones',
            'deadline' : 'Fecha límite',
            'status' : 'Estado',
            'task_tag' : 'Etiqueta',
        }
        widgets = {
            'deadline': forms.DateInput( attrs={'type': 'date' , 'value': f'{timezone.now().date()}'}),

        }

class EditTask(ModelForm):
   
    class Meta:
        model = Task
        exclude = ['task_owner']
        labels = {
            'title' : 'Título',
            'description' : 'Descripción y observaciones',
            'deadline' : 'Fecha límite',
            'status' : 'Estado', 
            'task_tag' : 'Etiqueta',
        }
        widgets = {
            
        }
    