from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task'),
    path('add', views.add_task, name='add'),
    path('remove', views.remove_task, name='remove'),
]
