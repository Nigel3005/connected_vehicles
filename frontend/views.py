import math

from django.http import JsonResponse
from django.shortcuts import render, redirect
# from future.backports.datetime import timedelta
from datetime import timedelta

from rest_framework.views import APIView

from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate, get_user_model
from django.shortcuts import render
from rest_framework.response import Response
import datetime as datetime
import numpy as np
from django.db import models

from api.models import vehicleStatus
from frontend.forms import SignUpForm, LoginForm


def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def dashboardView(request):
    if not request.user.is_anonymous:
        vehicle_ids = request.user.profile.vehicle_ids
        if vehicle_ids is not None:
            vehicle_ids_sep = split_vehicle_ids(vehicle_ids)
            selected_vehicle_id = get_selected_vehicle_id(request, vehicle_ids_sep)

            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id).order_by('time').reverse()
            if len(vehicle_statusses) > 0:
                args = {'page':'dashboard.html', 'vehicle_status': vehicle_statusses[0], 'vehicle_id': selected_vehicle_id}
                return render(request, 'default-without-footer.html', args)
            else:
                args = {'page': 'dashboard.html', 'vehicle_id': vehicle_ids}
                return render(request, 'default-without-footer.html', args)

    args = {'page': 'dashboard.html',}
    return render(request, 'default-without-footer.html', args)



def logboekView(request):
    if not request.user.is_anonymous:
        vehicle_ids = request.user.profile.vehicle_ids

        # check if user has vehicle ids in profile
        if vehicle_ids is not None:
            # Sepperate vehicle ids
            vehicle_ids_sep = split_vehicle_ids(vehicle_ids)

            # Get querys from request
            selected_column_names_unf = request.GET.get('column_names')
            selected_vehicle_id = get_selected_vehicle_id(request, vehicle_ids_sep)
            selected_startDate_unf = request.GET.get("startDate")
            selected_endDate_unf = request.GET.get("endDate")
            selected_page = request.GET.get("logboekpage")
            # Check if user filtered on vehicle id else set selected vehicle id to first vehicle id in profile
            if selected_vehicle_id is None:
                selected_vehicle_id = vehicle_ids_sep[0]

            if (selected_startDate_unf is None) or (selected_endDate_unf is None):
                now = datetime.datetime.now()
                start_date = datetime.datetime(now.year, now.month, now.day, 0, 0)
                end_date = datetime.datetime(now.year, now.month, now.day, 23, 59)
            else:
                start_date = datetime.datetime.strptime(selected_startDate_unf, '%d/%m/%Y %H:%M')
                end_date = datetime.datetime.strptime(selected_endDate_unf, '%d/%m/%Y %H:%M')
            date = (start_date, end_date)


            if selected_page is None:
                selected_page = 1


            # Get all vehicle statusses with selected vehicle id
            start = 100*(selected_page-1)
            end = start + 100
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id, time__range=date).order_by('time').reverse()
            n_pages = math.ceil(len(vehicle_statusses)/100)
            vehicle_statusses = vehicle_statusses[start:end]

            # Get all possible variables in model
            # column_names_all_unf = [f.name for f in vehicleStatus._meta.get_fields()]
            # column_names_all = format_column_names(column_names_all_unf)

            column_names_all_unf_unfilt = [f.name for f in vehicleStatus._meta.get_fields()]
            arr = np.array(list(column_names_all_unf_unfilt))
            filter_arr = []
            for element in arr:
                if (element == "vehicle_id"):
                    filter_arr.append(False)
                else:
                    filter_arr.append(True)
            column_names_all_unf = arr[filter_arr]
            column_names_all = format_column_names(column_names_all_unf)

            # Check if there are statusses with selected vehicle id
            status_matrix, column_names_form = [],[]
            if len(vehicle_statusses) > 0:
                # Check if user filtered on columns else use all column names
                if selected_column_names_unf is None:
                    column_names = column_names_all
                else:
                    column_names_unf = selected_column_names_unf.split(",")
                    column_names = format_column_names(column_names_unf)

                # Create table matrix
                for status in vehicle_statusses:
                    row = []
                    dict = vars(status)
                    for name in column_names:
                        row.append(dict[name[0]])
                    status_matrix.append(row)

            else:
                column_names = None

            # Render template
            args = {'page':'logboek.html',
                    'vehicle_statusses': status_matrix,
                    'vehicle_ids': vehicle_ids_sep,
                    'column_names': column_names,
                    'vehicle_id': selected_vehicle_id,
                    'column_names_all': column_names_all,
                    'chart_date_range': get_chart_date_range(),
                    'start_date': start_date.strftime('%d/%m/%Y %H:%M'),
                    'end_date': end_date.strftime('%d/%m/%Y %H:%M'),
                    'selected_page' : selected_page,
                    'pagelist': range(n_pages+1)[1:],
                    }
            return render(request, 'default-without-footer.html', args)

    # Render template without statusses and without vehicle id
    args = {'page': 'logboek.html'}
    return render(request, 'default-without-footer.html', args)

def profielView(request):
    if not request.user.is_anonymous:
        vehicle_id = request.user.profile.vehicle_ids
        if vehicle_id != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=vehicle_id).order_by('time').reverse()
            args = {'page': 'profiel.html', 'vehicle_statusses': vehicle_statusses, 'vehicle_id': vehicle_id}

            return render(request, 'default-without-footer.html', args)
        else:
            args = {'page': 'profiel.html', 'vehicle_statusses': None, 'vehicle_id': vehicle_id}
            return render(request, 'default-without-footer.html', args)
    else:
        args = {'page': 'profiel.html', 'vehicle_statusses': None}
        return render(request, 'default-without-footer.html', args)


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
    return render(request, 'default-without-footer.html', {'page': 'registration/register.html', 'form': form})

def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/dashboard')
                else:
                    form = LoginForm
                    return render(request, 'default-without-footer.html', {'page': 'registration/login.html', 'form': form, 'error': 'Account is not activated'})
            else:
                form = LoginForm
                return render(request, 'default-without-footer.html', {'page': 'registration/login.html', 'form': form, 'error': 'Your username and password were incorrect.'})
        except:
            form = LoginForm
            return render(request, 'default-without-footer.html', {'page': 'registration/login.html', 'form': form, 'error': 'Invalid Form'})

    else:
        form = LoginForm
        return render(request, 'default-without-footer.html', {'page': 'registration/login.html', 'form': form, 'error': ''})

def logoutView(request):
    logout(request)
    return redirect('Home')



def dataAnalyticsView(request):
    if not request.user.is_anonymous:
        vehicle_ids = request.user.profile.vehicle_ids

        # check if user has vehicle ids in profile
        if vehicle_ids is not None:
            # Sepperate vehicle ids
            vehicle_ids_sep = vehicle_ids.replace(" ","").split(";")
            vehicle_ids_sep = [n for n in vehicle_ids_sep if len(n) > 0] # Filter spaces

            # Get querys from request
            selected_vehicle_id = request.GET.get('vehicle_id')
            selected_column_names_unf = request.GET.get('column_names')
            selected_startDate_unf = request.GET.get("startDate")
            selected_endDate_unf = request.GET.get("endDate")

            # Check if user filtered on vehicle id else set selected vehicle id to first vehicle id in profile
            if selected_vehicle_id is None:
                selected_vehicle_id = vehicle_ids_sep[0]

            if (selected_startDate_unf is None) or (selected_endDate_unf is None):
                now = datetime.datetime.now()
                start_date = datetime.datetime(now.year,now.month,now.day,0,0)
                end_date = datetime.datetime(now.year,now.month,now.day,23,59)
            else:
                start_date = datetime.datetime.strptime(selected_startDate_unf, '%d/%m/%Y %H:%M')
                end_date = datetime.datetime.strptime(selected_endDate_unf, '%d/%m/%Y %H:%M')
            date = (start_date, end_date)

            # Get all vehicle statusses with selected vehicle id and selected date range
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id, time__range=date).order_by('time').reverse()

            # Get all possible variables in model
            column_names_all_unf_unfilt = [f.name for f in vehicleStatus._meta.get_fields()]
            arr = np.array(list(column_names_all_unf_unfilt))
            filter_arr = []
            for element in arr:
                if ((element == "vehicle_id") or (element == "time") or (element == 'id')):
                    filter_arr.append(False)
                else:
                    filter_arr.append(True)
            column_names_all_unf = arr[filter_arr]
            column_names_all = format_column_names(column_names_all_unf)

            # Check if there are statusses with selected vehicle id
            status_matrix, column_names_form = [],[]
            if len(vehicle_statusses) > 0:
                # Check if user filtered on columns else use all column names
                if selected_column_names_unf is None:
                    column_names = column_names_all
                else:
                    column_names_unf = selected_column_names_unf.split(",")
                    column_names = format_column_names(column_names_unf)

                # Create table matrix

                for status in vehicle_statusses:
                    row = []
                    dict = vars(status)
                    for name in column_names:
                        row.append(dict[name[0]])
                    status_matrix.append(row)

                charts = []

                for i in range(len(column_names)):
                    name_list = column_names[i]
                    name = name_list[0]
                    x, y = [], []
                    for s in range(len(status_matrix)):
                        row = status_matrix[s]
                        valx = vehicle_statusses[s].time.strftime('%Y-%m-%dT%H:%M:%S')
                        # valx = vehicle_statusses[s].time.timestamp()
                        # valx = vehicle_statusses[s].time.timestamp()
                        valy = float(row[i])
                        x.append(valx)
                        y.append(valy)
                    # x = list(range(len(y)))
                    chart = Chart(name, x, y)
                    charts.append(chart)
            else:
                column_names = None
                charts = None

            # Render template
            args = {'page':'data-analytics.html',
                    'vehicle_statusses': status_matrix,
                    'vehicle_ids': vehicle_ids_sep,
                    'column_names': column_names,
                    'vehicle_id': selected_vehicle_id,
                    'column_names_all': column_names_all,
                    'charts': charts,
                    'start_date': start_date.strftime('%d/%m/%Y %H:%M'),
                    'end_date': end_date.strftime('%d/%m/%Y %H:%M'),
                    }
            return render(request, 'default-without-footer.html', args)

    # Render template without statusses and without vehicle id
    args = {'page': 'data-analytics.html'}
    return render(request, 'default-without-footer.html', args)


# FUNCTIONS
def format_column_names(column_names_unf):
    column_names = [None] * len(column_names_unf)
    for i in range(len(column_names_unf)):
        unformatted = column_names_unf[i]
        formatted = unformatted.replace("_", " ").capitalize()
        column_names[i] = [unformatted, formatted]
    return column_names

def split_vehicle_ids(vehicle_ids):
    vehicle_ids_sep = vehicle_ids.replace(" ", "").split(";")
    vehicle_ids_sep = [n for n in vehicle_ids_sep if len(n) > 0]  # Filter spaces
    return vehicle_ids_sep

def get_selected_vehicle_id(request, vehicle_ids_sep):
    # get query vehicle id
    selected_vehicle_id = request.GET.get('vehicle_id')

    # Check if user filtered on vehicle id else set selected vehicle id to first vehicle id in profile
    if selected_vehicle_id is None:
        selected_vehicle_id = vehicle_ids_sep[0]

    return selected_vehicle_id

def get_chart_date_range():
    second_date = datetime.date.today()
    first_date = datetime.date(second_date.year,second_date.month-1,second_date.day)
    range_string = first_date.strftime('%m/%d/%Y') + " - " + second_date.strftime('%m/%d/%Y')

    return range_string


class Chart:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y