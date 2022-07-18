from django.urls import path
from crud_problems_app import views

urlpatterns = [
    path('home/read/',views.read_problems, name="read"),
    path('home/create/',views.create_problems, name="create"),
    path('home/update/<str:id>/',views.update_problems, name="update"),
    path('home/delete/<str:id>/',views.delete_problems, name="delete"),
]