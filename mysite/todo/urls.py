from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/tasks', views.list_tasks, name='list-task'),
    path('api/v1/tasks', views.add_task, name='add'),
    path('api/v1/tasks', views.search, name='get'),
    path('api/v1/tasks/<int:task_id>', views.remove_task, name='remove'),
    path('api/v1/tasks/{task-id}', views.update_task, name='update'),
]
