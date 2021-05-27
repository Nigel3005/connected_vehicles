from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from api.models import vehicleStatus
from frontend.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
import pandas as pd
from matplotlib import pyplot as plt



def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def statusView(request):
    if not request.user.is_anonymous:
        vehicle_id = request.user.profile.vehicle_ids
        if vehicle_id != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=vehicle_id).order_by('time').reverse()
            args = {'page':'status.html', 'vehicle_statusses': vehicle_statusses, 'vehicle_id': vehicle_id}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'status.html', 'vehicle_statusses': None, 'vehicle_id': vehicle_id}
            return render(request, 'default.html', args)
    else:
        args = {'page': 'status.html', 'vehicle_statusses': None}
        return render(request, 'default.html', args)



def logboekView(request):
    if not request.user.is_anonymous:
        vehicle_ids = request.user.profile.vehicle_ids
        if vehicle_ids != None:
            # Sepperate vehicle statusses
            vehicle_ids_sep = vehicle_ids.replace(" ","").split(";")
            vehicle_ids_sep = [n for n in vehicle_ids_sep if len(n) > 0] # Filter empty
            selected_vehicle_id = request.GET.get('vehicle_id')
            if selected_vehicle_id == None:
                selected_vehicle_id = vehicle_ids_sep[0]
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id).order_by('time').reverse()
            status_matrix = []
            if len(vehicle_statusses) > 0:
                column_names = [f.name for f in vehicleStatus._meta.get_fields()]
                column_names_form = [name.replace("_", " ").capitalize() for name in column_names]
                for status in vehicle_statusses:
                    row = []
                    for name in column_names:
                        row.append(exec("status." + str(name)))
                    status_matrix.append(row)

            else:
                column_names = None

            # Render template
            args = {'page':'logboek.html', 'vehicle_statusses': status_matrix, 'vehicle_ids': vehicle_ids_sep, 'column_names': column_names_form, 'vehicle_id': selected_vehicle_id}
            return render(request, 'default.html', args)

    # Render template without statusses and without vehicle id
    args = {'page': 'logboek.html'}
    return render(request, 'default.html', args)

def profielView(request):
    if not request.user.is_anonymous:
        vehicle_id = request.user.profile.vehicle_ids
        if vehicle_id != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=vehicle_id).order_by('time').reverse()
            args = {'page': 'profiel.html', 'vehicle_statusses': vehicle_statusses, 'vehicle_id': vehicle_id}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'profiel.html', 'vehicle_statusses': None, 'vehicle_id': vehicle_id}
            return render(request, 'default.html', args)
    else:
        args = {'page': 'profiel.html', 'vehicle_statusses': None}
        return render(request, 'default.html', args)


def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Login')
    else:
        form = SignUpForm()
    return render(request, 'default.html', {'page': 'registration/register.html', 'form': form})

def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home')
                else:
                    form = LoginForm
                    return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Account is not activated'})
            else:
                form = LoginForm
                return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Your username and password were incorrect.'})
        except:
            form = LoginForm
            return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Invalid Form'})

    else:
        form = LoginForm
        return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': ""})

def logoutView(request):
    logout(request)
    return redirect('Home')



def analyticsView(request):
    if not request.user.is_anonymous:
        vehicle_id = request.user.profile.vehicle_ids
        if vehicle_id != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=vehicle_id).order_by('time').reverse()
            args = {'page':'data-analytics.html', 'vehicle_statusses': vehicle_statusses, 'vehicle_id': vehicle_id}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'data-analytics.html', 'vehicle_statusses': None, 'vehicle_id': vehicle_id}
            return render(request, 'default.html', args)
    else:
        args = {'page': 'data-analytics.html', 'vehicle_statusses': None}
        return render(request, 'default.html', args)