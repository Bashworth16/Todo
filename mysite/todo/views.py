from django.shortcuts import render
from .models import Todo


def task_list(request):
    objects_list = Todo.objects.all()
    context = {
        'List': objects_list
    }
    return render(request, 'todos/index.html', context)


def add_task(request):
    if request.method == 'POST':
        new_task = Todo()
        new_task.task = request.POST.get('add_task')
        new_task.save()
        return render(request, 'todos/add_task.html')
    else:
        return render(request, 'todos/add_task.html')


def remove_task(request, id=None):
    deleted = Todo.objects.filter(id=id).delete()
    return render(request, 'todos/remove.html', deleted)
