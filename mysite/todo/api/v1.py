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
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def request_task(request, task_id):
    if request.method == "GET":
        return get_task(task_id)
    if request.method == "DELETE":
        return delete_task(task_id)
    if request.method == "PUT":
        return put_task(request, task_id)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'])


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
    print(type(j_task))
    print(j_task.keys())
    print(type(j_task.get('task')))
    print(j_task.get('task'))
    new_task.task = j_task.get('task')
    print(new_task.task)
    print(type(new_task.task))
    new_task.save()
    return JsonResponse({
        "items": j_task,
    }, safe=True)


@csrf_exempt
def get_task(task_id):
    return_task = Todo.objects.filter(id=task_id)
    return JsonResponse({
        "items": list(return_task),
    }, safe=True)


@csrf_exempt
def delete_task(task_id):
    Todo.objects.filter(id=task_id).delete()
    return HttpResponse()


@csrf_exempt
def put_task(request, task_id):
    task_text = request.body.decode('utf-8')
    j_task = json.loads(task_text)
    update = Todo()
    update.id = task_id
    update.task = j_task.get('task')
    update.save()
    return HttpResponse()
