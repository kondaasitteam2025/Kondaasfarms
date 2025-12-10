from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employee_list, name='employee_list'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('assets/', views.asset_list, name='asset_list'),
    path('cows/', views.cow_list, name='cow_list'),
]
