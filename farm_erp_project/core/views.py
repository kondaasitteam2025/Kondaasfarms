from django.shortcuts import render, redirect
from .models import Employee, Inventory, Asset, Cow
def index(request):
    return redirect('core:employee_list')
def employee_list(request):
    qs = Employee.objects.select_related('assigned_valve').all()
    return render(request, 'core/employee_list.html', {'employees': qs})
def inventory_list(request):
    qs = Inventory.objects.all()
    return render(request, 'core/inventory_list.html', {'inventory': qs})
def asset_list(request):
    qs = Asset.objects.all()
    return render(request, 'core/asset_list.html', {'assets': qs})
def cow_list(request):
    qs = Cow.objects.all()
    return render(request, 'core/cow_list.html', {'cows': qs})
