from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .forms.task.forms import CreateTask, EditTask 
from .models import Task, Tag
from user_manager.forms.forms import CustomCreationForm

def home(request):
    dataTime = timezone.now().date()
    return render(request, 'task/home.html', {
        # 'form' : CustomCreationForm
        'dataTime' : dataTime
    })
  


@login_required
def task(request, typ=None, prio=None):

    formCreateTask = CreateTask()

    tasks_pending = Task.objects.filter(task_owner=request.user, status='Pendiente')
    tasks_inprogress = Task.objects.filter(task_owner=request.user, status='En progreso')
    tasks_completed = Task.objects.filter(task_owner=request.user, status='Completada')
    tasks_expired = Task.objects.filter(deadline__lt=timezone.now().date())
    tasks_filterTag = Task.objects.filter(task_tag=typ)
    task_filterPriority = Task.objects.filter(task_priority_id=prio)

    pending_tasks = tasks_pending.count()
    inprogress_tasks = tasks_inprogress.count()
    completed_tasks = tasks_completed.count()
    expired_tasks = tasks_expired.count()
    is_expired = False
    select_filter = request.GET.get('filter_option')
    
    
    if prio != None:
        is_expired = False
        tasks = task_filterPriority.order_by('deadline')
      
        title_list = f'estas tareas estan filtradas por prioridad.'
        formCreateTask = CreateTask()
        return render(request, 'task/task.html', {
            'tasks' : tasks,
            'formCreateTask': formCreateTask,
            'title_list' : title_list,
            'is_expired' : is_expired,
            'pending_tasks' : pending_tasks, 
            'inprogress_tasks' : inprogress_tasks,
            'completed_tasks' : completed_tasks,
            'expired_tasks' : expired_tasks
        })    
       
    if typ != None:
        is_expired = False
        tasks =  tasks_filterTag.order_by('deadline')
      
        title_list = f'estas tareas estan filtradas por etiqueta.'
        formCreateTask = CreateTask()
        return render(request, 'task/task.html', {
            'tasks' : tasks,
            'formCreateTask': formCreateTask,
            'title_list' : title_list,
            'is_expired' : is_expired,
            'pending_tasks' : pending_tasks, 
            'inprogress_tasks' : inprogress_tasks,
            'completed_tasks' : completed_tasks,
            'expired_tasks' : expired_tasks
        })

    if select_filter == 'inprogress':
        tasks =  tasks_inprogress .order_by('deadline')
        title_list = 'estas son tus tareas en progreso.'
     
    elif select_filter == 'completed':
        tasks = tasks_completed.order_by('deadline')
        title_list = 'estas son tus tareas completadas'
        
    elif select_filter == 'expired':
        tasks = tasks_expired
        title_list = 'estas son tus tareas expiradas'
        is_expired = True
        
    else:
        tasks = tasks_pending.order_by('deadline')
        title_list = 'estas son tus tareas pendientes.'
        tasks_pending = tasks.count()
        
    
    
    return render(request, 'task/task.html', {
        'tasks' : tasks,
        'formCreateTask': formCreateTask,
        'title_list' : title_list,
        'is_expired' : is_expired,
        'pending_tasks' : pending_tasks, 
        'inprogress_tasks' : inprogress_tasks,
        'completed_tasks' : completed_tasks,
        'expired_tasks' : expired_tasks
    })



@login_required
def create(request, id):
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            selected_owner_id = form.cleaned_data['assigned_to']
            task = form.save(commit=False)
            if selected_owner_id != None:
                task.task_owner_id = selected_owner_id.id
            else:
                 task.task_owner_id = id
            task.save()
            return redirect('task')
        
    return render(request, 'task/createTask.html', {
         'form' : CreateTask()
    })

@login_required
def detail(request, id):
    taskDetail = get_object_or_404(Task, id=id)
    return render(request, 'task/detail.html', {
        'taskDetail': taskDetail
    })

@login_required
def edit(request, id):
    task =  get_object_or_404(Task, id=id)
    if request.method == 'GET':
        formEditTask = EditTask(instance=task)
        return render(request, 'task/editTask.html', {
            "formEditTask" : formEditTask
        })
    if request.method == 'POST':
        editTask= EditTask(request.POST, instance=task)
        if editTask.is_valid():
            editTask.save()
            return redirect('task')
    else:
        messages.error('Ha ocurrido un error, vuelva a intentarlo')
        return render(request, 'task/editTask.html', {
            'formEditTask' : formEditTask
        })

@login_required
def delete(request, id):
    taskDelete = get_object_or_404(Task, id=id)
    taskDelete.delete()
    return redirect('task')