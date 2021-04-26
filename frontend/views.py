from django.shortcuts import render, redirect
from django.contrib.sites import requests
from django.http import HttpResponse
from rest_framework import viewsets, request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render
from api.models import vehicleStatus
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)

@login_required
def status(request):
    template_name = 'status.html'
    vehicle_id = request.user.profile.vehicle_id
    vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=vehicle_id)
    args = {'vehicle_statusses': vehicle_statusses, 'vehicle_id':vehicle_id}
    return render(request, template_name, args)