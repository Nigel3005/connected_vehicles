from django.urls import path, include
from . import views

urlpatterns = [
    path('status', views.statusView, name='Status'),
    path('logboek', views.logboekView, name='Logboek'),
    path('', views.indexView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('register', views.registerView, name="Register"),
]