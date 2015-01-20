from django.shortcuts import render
from django.http import HttpResponse

from compute.models import DistributedTask

def index(request):
    return render(request, 'compute/index.html', {'message': "compute index."})

def test(request):
    return render(request, 'compute/test.html', {})

def tasks(request):
    tasks = DistributedTask.objects.all
    return render(request, 'compute/tasks.html', {'tasks': tasks})

def task(request):
    task = get_object_or_404(DistributedTask, pk=task_id)
    # question = Question.objects.get(pk=question_id)
    return render(request, 'compute/task.html', {'task': task})

