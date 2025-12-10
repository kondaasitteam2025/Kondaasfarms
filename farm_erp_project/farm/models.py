from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='plants/', blank=True, null=True)
    area_acres = models.FloatField(default=0)
    def __str__(self):
        return self.name

class Filter(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Valve(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    plant_count = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.filter.name} - {self.name}"
