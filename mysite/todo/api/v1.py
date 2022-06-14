from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo
from django.http import JsonResponse
import json
from django.http import HttpResponseNotAllowed, HttpResponse


@csrf_exempt
def request_tasks(request):
    if request.method == "GET":
        return get_tasks()
    if request.method == "POST":
        return post_task(request)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'], status=404)


@csrf_exempt
def request_task(request, task_id):
    if request.method == "GET":
        return get_task(task_id)
    if request.method == "DELETE":
        return delete_task(task_id)
    if request.method == "PUT":
        return put_task(request, task_id)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'], status=404)


@csrf_exempt
def get_tasks():
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def post_task(request):
    new_task = Todo()
    task_text = request.body.decode('utf-8')
    j_task = json.loads(task_text)
    new_task.task = j_task.get('task')
    new_task.save()
    return JsonResponse({
        'id': new_task.id,
        'task': new_task.task
    }, safe=True)


@csrf_exempt
def get_task(task_id):
    return_task = list(Todo.objects.filter(id=task_id).values())
    for val in return_task:
        return_task = val
    if return_task:
        return JsonResponse({
            'id': return_task.get('id'),
            'task': return_task.get('task')
        })
    else:
        return HttpResponse(status=404)


@csrf_exempt
def delete_task(task_id):
    Todo.objects.filter(id=task_id).delete()
    return HttpResponse(status=204)


@csrf_exempt
def put_task(request, task_id):
    task_text = request.body.decode('utf-8')
    j_task = json.loads(task_text)
    update = Todo()
    update.id = task_id
    update.task = j_task.get('task')
    update.save()
    return HttpResponse(status=204)
