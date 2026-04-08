from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncDate
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MeterReading

# Create your views here.
class DailyUsageView(APIView):
    def get(self, request):
        data = (
            MeterReading.objects
            .annotate(date=TruncDate('timestamp'))  # Extract only the date from the timestamp
            .values('date')                         # Group results by date
            .annotate(total_kwh = Sum('kwh'))       # Sum total of kwh of the day
            .order_by('date')                       # Sorts results chronologically
            )

        return Response(data)