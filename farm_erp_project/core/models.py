from django.db import models
from farm.models import Valve

class Employee(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True, null=True)
    assigned_valve = models.ForeignKey(Valve, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=20, default='nos')
    image = models.ImageField(upload_to='inventory/', blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    price_per_unit = models.FloatField(default=0)
    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    purchase_date = models.DateField()
    image = models.ImageField(upload_to='assets/', blank=True, null=True)
    def __str__(self):
        return self.name

class Cow(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    milk_per_day = models.FloatField(default=0)
    def __str__(self):
        return self.name
