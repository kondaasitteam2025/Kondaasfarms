from django.urls import path
from . import views
app_name = 'farm'
urlpatterns = [
    path('', views.index, name='index'),
    path('plants/', views.plant_list, name='plant_list'),
    path('filters/', views.filter_list, name='filter_list'),
    path('valves/', views.valve_list, name='valve_list'),
]
