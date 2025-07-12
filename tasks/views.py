from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST  # required for POST-only view

# 🏠 Task List View
def taskList(request):
    tasks = Task.objects.order_by('-created') 
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

# ✅ Checkbox Toggle View
@require_POST
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')

# Delete Task View
@require_POST
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('/')

#Edit Task View
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
