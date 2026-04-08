from django.db import models

## Base class of an Energy Meter
class Meter(models.Model):
    # The name, as a string with a set maximum length
    name = models.CharField(max_length=100)

    # Define how this object is displayed as a string by django
    def __str__(self):
        return self.name

## Every Meter will have a Meter Reading, which will consist of time of the reading, and the kwh reading
class MeterReading(models.Model):
    # Define the relationship between the MeterReading and the Meter classes.
    # "related_name=" allows a Meter object to easily look/access properties from the MeterReading
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name="readings")
    timestamp = models.DateTimeField()
    kwh = models.FloatField()

    # Define how this object is displayed as a string by django
    def __str__(self):
        return f"{self.meter.name} - {self.timestamp} - {kwh} kwh"
