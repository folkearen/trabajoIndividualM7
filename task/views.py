from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms.task.forms import CreateTask 
from .models import Task
from user_manager.forms.forms import CustomCreationForm

def home(request):
    return render(request, 'task/home.html', {
        # 'form' : CustomCreationForm
    })


@login_required
def task(request):
    tasks = Task.objects.filter(task_owner=request.user)
    formCreateTask = CreateTask()
    return render(request, 'task/task.html', {
        'tasks' : tasks,
        'formCreateTask': formCreateTask
    })

@login_required
def create(request, id):
    print(id)
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_owner_id = id
            task.save()
            return redirect('task')
    return render(request, 'task/createTask.html', {
        'form': CreateTask()
    })

@login_required
def detail(request, id):
    taskDetail = get_object_or_404(Task, id=id)
    return render(request, 'task/detail.html', {
        'taskDetail': taskDetail
    })