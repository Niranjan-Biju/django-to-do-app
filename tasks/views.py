from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST  # required for POST-only view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# 🏠 Task List View
@login_required
def taskList(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')

    return render(request, 'tasks/list.html', {'tasks': tasks, 'form': form})

# ✅ Checkbox Toggle View
@require_POST
@login_required
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')

# Delete Task View
@require_POST
@login_required
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('/')

#Edit Task View
@login_required
def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit.html', {'form': form, 'task': task})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})