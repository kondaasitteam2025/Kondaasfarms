from django.contrib import admin
from .models import Employee, Inventory, Asset, Cow
admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Asset)
admin.site.register(Cow)
