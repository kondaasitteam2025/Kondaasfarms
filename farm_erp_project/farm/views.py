from django.shortcuts import render, redirect
from .models import Plant, Filter, Valve
def index(request):
    return redirect('farm:plant_list')
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'farm/plant_list.html', {'plants': plants})
def filter_list(request):
    filters = Filter.objects.all()
    return render(request, 'farm/filter_list.html', {'filters': filters})
def valve_list(request):
    valves = Valve.objects.select_related('filter','plant').all()
    return render(request, 'farm/valve_list.html', {'valves': valves})
