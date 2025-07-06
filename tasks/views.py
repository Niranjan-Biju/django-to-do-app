from django.shortcuts import render
from .models import Task

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})
