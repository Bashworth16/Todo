from django.urls import path
from todo.views import index
from todo.api.v1 import request_tasks, request_task


urlpatterns = [
    path('home', index, name='home'),
    path('api/v1/tasks', request_tasks, name='index'),
    path('api/v1/task/<int:task_id>', request_task, name='id'),
]
