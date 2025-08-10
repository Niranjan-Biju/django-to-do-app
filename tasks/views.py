from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST  # required for POST-only view
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
            return redirect('tasks')  # your URL name

    return render(request, 'tasks/list.html', {'tasks': tasks, 'form': form})

@require_POST
@login_required
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.user != request.user:
        raise Http404()
    task.completed = not task.completed
    task.save()
    return redirect('tasks')

@require_POST
@login_required
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.user != request.user:
        raise Http404()
    task.delete()
    return redirect('tasks')

@login_required
def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.user != request.user:
        raise Http404()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit.html', {'form': form, 'task': task})

