from django.shortcuts import render
from django.db.models import QuerySet, Sum, F
from django.db.models.functions import TruncDate
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Meter, MeterReading

# Create your views here.
class DailyUsageView(APIView):
    def get(self, request):
        # Define a Meter Id so we can filter the dailyusageview by the individual meter
        meter_id = request.query_params.get('meter_id')
        QuerySet = MeterReading.objects.all() # Changed to QuerySet so we have access to more query parameters
        if meter_id:
            QuerySet = QuerySet.filter(meter_id=meter_id)

        data = (
            QuerySet
            .annotate(date=TruncDate('timestamp'))  # Extract only the date from the timestamp
            .values('date')                         # Group results by date
            .annotate(
                total_kwh = Sum('kwh'),              # Sum total of kwh of the day
                total_cost =Sum(F('kwh') * F('meter__tariff__price_per_kwh')) # Second F() finds the meter -> tariff -> price_per_kwh
                )       
            .order_by('date')                       # Sorts results chronologically
            )

        return Response(data)