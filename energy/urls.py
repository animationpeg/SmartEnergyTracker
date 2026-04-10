from django.urls import path
from .views import DailyUsageView, HourlyUsageView

urlpatterns = [
    path('daily-usage/', DailyUsageView.as_view()),
    path('hourly-usage/', HourlyUsageView.as_view()),
]