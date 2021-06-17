from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.indexView, name='Home'),
    path('status', views.statusView, name='Status'),
    path('logboek', views.logboekView, name='Logboek'),
    path('profiel', views.profielView, name='Profiel'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('register', views.registerView, name="Register"),
    path('data-analytics', views.dataAnalyticsView, name='Data-Analytics'),
]