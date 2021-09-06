from django.urls import path
from training_app import views

urlpatterns = [
    path('home/question/',views.practice_problem, name="question"),
]