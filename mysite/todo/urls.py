from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task'),
    path('add', views.add_task, name='add'),
    path('results', views.search, name='search1'),
    path('remove/<task_id>/', views.remove_task, name='remove'),
    path('update1/<task_id>/', views.update1, name='update'),
    path('update1/<task_id>/update_task', views.update_task, name='update_task'),
]
