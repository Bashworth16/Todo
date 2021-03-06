from django.urls import path
from todo.api.v1 import request_tasks, request_task

urlpatterns = [
    path('api/v1/tasks', request_tasks, name='index'),
    path('api/v1/task/<int:task_id>', request_task, name='id'),
]
