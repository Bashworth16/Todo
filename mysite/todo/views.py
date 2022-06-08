from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http import JsonResponse
import json


@csrf_exempt
def get_tasks():
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def post_task(request):
    new_task = Todo()
    task_text = request.body.decode('utf-8')
    jtask = json.loads(task_text)
    new_task.task = jtask.get('task')
    new_task.save()
    return JsonResponse({
        "items": list(Todo.objects.values()),
    }, safe=True)


@csrf_exempt
def get_task(task_id):
    return JsonResponse({
        "items": list(Todo.objects.filter(id=task_id)),
    }, safe=True)


@csrf_exempt
def delete_task(task_id):
    Todo.objects.filter(id=task_id).delete()
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def put_task(request, task_id):
    uptask = Todo.objects.get(id=task_id)
    uptask.task = request.GET.get('text_update')
    uptask.save()
    return JsonResponse({
        "items": list(Todo.objects.all()),
    }, safe=True)
