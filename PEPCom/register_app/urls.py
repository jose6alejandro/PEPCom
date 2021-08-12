from django.urls import path
from register_app import views

urlpatterns = [
    path('accounts/login/', views.login, name="login"),
    path('home/', views.home, name="home"),
]