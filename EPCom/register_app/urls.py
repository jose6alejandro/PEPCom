from django.urls import path
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from register_app import views

urlpatterns = [
	#url(r'^accounts/login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/login.html'), name="logout"),
    path('accounts/login/', views.login_view, name="login"),
    path('home/', login_required(views.home), name="home"),
    path('', views.redirect_home, name="redirect_home"),
]