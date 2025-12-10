from django.shortcuts import render, redirect
from .models import FertigationTask, WaterFlow, WildBoarAttack
from .forms import FertigationTaskForm
from datetime import date

def index(request):
    return redirect('fertigation:task_list')

def task_list(request):
    tasks = FertigationTask.objects.select_related('valve','plant').all().order_by('-scheduled_date')
    return render(request, 'fertigation/fertigation_task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = FertigationTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fertigation:task_list')
    else:
        form = FertigationTaskForm(initial={'scheduled_date': date.today()})
    return render(request, 'fertigation/task_create.html', {'form': form})

def waterflow_list(request):
    flows = WaterFlow.objects.select_related('valve').all().order_by('-measured_on')[:200]
    return render(request, 'fertigation/waterflow_list.html', {'flows': flows})

def wildboar_list(request):
    attacks = WildBoarAttack.objects.select_related('plant').all().order_by('-date')
    return render(request, 'fertigation/wildboar_list.html', {'attacks': attacks})
