from django.urls import path
from .views import DailyUsageView

urlpatterns = [
    path('daily-usage/', DailyUsageView.as_view()),
]