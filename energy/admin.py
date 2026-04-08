from django.contrib import admin
from .models import Meter, MeterReading

# Register your models here.
admin.site.register(Meter)
admin.site.register(MeterReading)
