from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from compute.models import DistributedTask

def index(request):
    return render(request, 'compute/index.html', {'message': "compute index."})

def test(request):
    return render(request, 'compute/test.html', {})

def tasks(request):
    tasks = DistributedTask.objects.all
    return render(request, 'compute/tasks.html', {'tasks': tasks})

def task(request, task_id):
    task = get_object_or_404(DistributedTask, pk=task_id)
    # question = Question.objects.get(pk=question_id)
    return render(request, 'compute/task.html', {'task': task})

def new_task(request):
    task = DistributedTask()
    # question = Question.objects.get(pk=question_id)
    return render(request, 'compute/task.html', {'task': task})

def save_task(request):
    task = DistributedTask()
    task.name = "task"
    task.map_func = request.POST.get("map_func")
    task.reduce_func = request.POST.get("reduce_func")
    task.then_func = request.POST.get("then_func")
    task.data = request.POST.get("data") or ""
    task.save()
    return render(request, 'compute/task.html', {'task': task})

