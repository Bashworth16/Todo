from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http import JsonResponse


@csrf_exempt
def list_tasks(request):
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def search(request):
    if request.method == 'GET':
        s = request.GET.get('search_text')
        results = ''
        for task in Todo.objects.all():
            if s == task.id:
                results = task
            else:
                pass
        return JsonResponse({
            "items": list(Todo.objects.filter(results)),
        })
    else:
        return JsonResponse({
            "items": list(Todo.objects.filter()),
        })


@csrf_exempt
def add_task(request):
    if request.POST:
        new_task = Todo()
        new_task.task = request.POST.get('add_task')
        new_task.save()
        return JsonResponse({
            "items": list(Todo.objects.values()),
        })
    else:
        return JsonResponse({
            "items": list(Todo.objects.values()),
        })


@csrf_exempt
def remove_task(request, task_id):
    Todo.objects.filter(id=task_id).delete()
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def update_task(request, task_id):
    uptask = Todo.objects.get(id=task_id)
    uptask.task = request.PUT.get('text_update')
    uptask.save()
    return JsonResponse({
        "items": list(Todo.objects.all()),
    })
