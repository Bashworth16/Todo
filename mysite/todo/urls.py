from django.urls import path
from mysite.todo.api.v1 import *


urlpatterns = [
    path('api/v1/tasks', get_tasks, name='index'),
    path('api/v1/tasks/<int:task_id>', get_task, name='id'),
]
