from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from ...models import Task 



class CreateTask(ModelForm):

    class Meta:
        model = Task
        exclude = ['task_owner','status']
        labels = {
            'title' : 'Título',
            'description' : 'Descripción y observaciones',
            'deadline' : 'Fecha límite',
            'status' : 'Estado',
            'task_priority': 'Prioridad',
            'task_tag' : 'Etiqueta',
            'assigned_to' : 'Si desea asignar la tarea a otro usuario seleccionelo:'
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
            'task_priority': 'Prioridad',
            'task_tag' : 'Etiqueta',
            'assigned_to' : 'Si desea asignar la tarea a otro usuario seleccionelo:',
        }
