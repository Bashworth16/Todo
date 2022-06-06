from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http import JsonResponse, HttpResponseNotAllowed


@csrf_exempt
def request_sort(request):
    if request.method == "GET":
        print(request.method)
        return list_tasks()
    if request.method == "POST":
        print(request.method)
        return add_task(request)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def request_sort_with_id(request, task_id):
    if request.method == "GET":
        print(request.method)
        return get(task_id)
    if request.method == "DELETE":
        print(request.method)
        return remove_task(task_id)
    if request.method == "PUT":
        print(request.method)
        return update_task(request, task_id)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'])


@csrf_exempt
def list_tasks():
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def add_task(request):
    new_task = Todo()
    new_task.task = request.POST.get('key')
    new_task.save()
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def get(task_id):
    return JsonResponse({
        "items": list(Todo.objects.filter(id=task_id)),
    })


@csrf_exempt
def remove_task(task_id):
    Todo.objects.filter(id=task_id).delete()
    return JsonResponse({
        "items": list(Todo.objects.values()),
    })


@csrf_exempt
def update_task(request, task_id):
    uptask = Todo.objects.get(id=task_id)
    uptask.task = request.GET.get('text_update')
    uptask.save()
    return JsonResponse({
        "items": list(Todo.objects.all()),
    })
