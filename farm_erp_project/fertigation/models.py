from django.db import models
from farm.models import Plant, Valve

class FertigationTask(models.Model):
    valve = models.ForeignKey(Valve, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=120, blank=True)
    scheduled_date = models.DateField()
    actual_work_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('Pending','Pending'),('Done','Done')], default='Pending')
    fertilizer_quantity = models.FloatField(default=0)
    fertilizer_unit = models.CharField(max_length=10, default='kg')
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='tasks/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.actual_work_date:
            self.status = 'Done' if self.actual_work_date == self.scheduled_date else 'Pending'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Task {self.id} - {self.plant.name} - {self.valve.name}"

class WaterFlow(models.Model):
    valve = models.ForeignKey(Valve, on_delete=models.CASCADE)
    flow_rate = models.FloatField(help_text='Litres per hour')
    measured_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.valve} @ {self.measured_on}"

class WildBoarAttack(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateField()
    damage_level = models.CharField(max_length=50, choices=[('Low','Low'),('Medium','Medium'),('High','High')])
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.plant.name} - {self.date}"
