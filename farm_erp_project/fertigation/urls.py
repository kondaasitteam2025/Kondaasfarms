from django.urls import path
from . import views
app_name = 'fertigation'
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('waterflow/', views.waterflow_list, name='waterflow_list'),
    path('wildboar/', views.wildboar_list, name='wildboar_list'),
]
