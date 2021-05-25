from django.urls import path
from . import views

urlpatterns = [
    path('status', views.statusView, name='status'),
    path('', views.indexView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('register', views.registerView, name="Register"),
]