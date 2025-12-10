from django import forms
from .models import FertigationTask
class FertigationTaskForm(forms.ModelForm):
    class Meta:
        model = FertigationTask
        fields = ['valve','plant','employee_name','scheduled_date','actual_work_date','fertilizer_quantity','fertilizer_unit','photo','notes']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type':'date','readonly':'readonly'}),
            'actual_work_date': forms.DateInput(attrs={'type':'date'}),
        }
