from django.contrib import admin
from django.urls import path
from .views import viewVehicleStatusses

urlpatterns = [
    path('view-vehicle-statusses/', viewVehicleStatusses.as_view()),
]
