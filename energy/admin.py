from django.contrib import admin
from .models import Meter, MeterReading, Tariff

# Register your models here.
admin.site.register(Tariff)
admin.site.register(Meter)
admin.site.register(MeterReading)
