from django.urls import path
from statistics_app import views

urlpatterns = [
    path('home/stats/',views.my_stats, name="stats"),
    path('home/statistics/',views.all_stats, name="statistics"),
    path('home/stats/view/<str:id>/',views.view_select_stats, name="stats_view")
]