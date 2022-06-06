from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/tasks', views.request_sort, name='index'),
    path('api/v1/tasks/<int:task_id>', views.request_sort_with_id, name='id'),
]
