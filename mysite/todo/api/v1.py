from django.views.decorators.csrf import csrf_exempt
from .views import get_task, get_tasks, post_task, put_task, delete_task
from django.http import HttpResponseNotAllowed


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
