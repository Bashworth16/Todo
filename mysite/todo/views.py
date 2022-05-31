from django.shortcuts import render
from .models import Todo


def task_list(request):
    objects_list = Todo.objects.all()
    context = {
        'List': objects_list
    }
    return render(request, 'todos/index.html', context)


def search(request):
    search_text = request.POST.get('search_text')
    results1 = ''
    for jobs in Todo.objects.all():
        if search_text == jobs.task:
            results1 = jobs.task
        else:
            pass
    context = {
        'results': results1
    }
    return render(request, 'todos/results.html', context)


def add_task(request):
    if request.method == 'POST':
        new_task = Todo()
        new_task.task = request.POST.get('add_task')
        new_task.save()
        return render(request, 'todos/add_task.html')
    else:
        return render(request, 'todos/add_task.html')


def remove_task(request, task_id):
    Todo.objects.filter(id=task_id).delete()
    return render(request, 'todos/remove.html')


def update1(request, task_id):
    return render(request, 'todos/update.html')


def update_task(request, task_id):
    uptask = Todo.objects.get(id=task_id)
    uptask.task = request.POST.get('text_update')
    uptask.save()
    return render(request, 'todos/update_task.html')
