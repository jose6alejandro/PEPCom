from django.urls import path
from statistics_app import views

urlpatterns = [
    path('home/stats/',views.my_stats, name="stats"),
]