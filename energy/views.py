from django.shortcuts import render
from django.db.models import QuerySet, Sum
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
            .annotate(total_kwh = Sum('kwh'))       # Sum total of kwh of the day
            .order_by('date')                       # Sorts results chronologically
            )

        return Response(data)