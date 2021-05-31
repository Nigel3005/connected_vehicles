from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from api.models import vehicleStatus
from frontend.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render



def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def statusView(request):
    if not request.user.is_anonymous:
        vehicle_ids = request.user.profile.vehicle_ids
        if vehicle_ids is not None:
            vehicle_ids_sep = split_vehicle_ids(vehicle_ids)
            selected_vehicle_id = get_selected_vehicle_id(request, vehicle_ids_sep)

            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id).order_by('time').reverse()
            if len(vehicle_statusses) > 0:
                args = {'page':'status.html', 'vehicle_status': vehicle_statusses[0], 'vehicle_id': selected_vehicle_id}
                return render(request, 'default.html', args)
            else:
                args = {'page': 'status.html', 'vehicle_id': vehicle_id}
                return render(request, 'default.html', args)

    args = {'page': 'status.html',}
    return render(request, 'default.html', args)



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

            # Get all vehicle statusses with selected vehicle id
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id).order_by('time').reverse()

            # Get all possible variables in model
            column_names_all_unf = [f.name for f in vehicleStatus._meta.get_fields()]
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
            args = {'page':'logboek.html', 'vehicle_statusses': status_matrix, 'vehicle_ids': vehicle_ids_sep, 'column_names': column_names, 'vehicle_id': selected_vehicle_id, 'column_names_all': column_names_all}
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
                    return redirect('/status')
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
        return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': '' })

def logoutView(request):
    logout(request)
    return redirect('Home')



def analyticsView(request):
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

            # Check if user filtered on vehicle id else set selected vehicle id to first vehicle id in profile
            if selected_vehicle_id is None:
                selected_vehicle_id = vehicle_ids_sep[0]

            # Get all vehicle statusses with selected vehicle id
            vehicle_statusses = vehicleStatus.objects.filter(vehicle_id=selected_vehicle_id).order_by('time').reverse()

            # Get all possible variables in model
            column_names_all_unf = [f.name for f in vehicleStatus._meta.get_fields()]
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
            args = {'page':'logboek.html', 'vehicle_statusses': status_matrix, 'vehicle_ids': vehicle_ids_sep, 'column_names': column_names, 'vehicle_id': selected_vehicle_id, 'column_names_all': column_names_all}
            return render(request, 'default.html', args)

    # Render template without statusses and without vehicle id
    args = {'page': 'logboek.html'}
    return render(request, 'default.html', args)


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
# def get_data(request, *args, **kwargs):
#     data = {
#         "sales": 100,
#         "customers": 10,
#     }
#     return JsonResponse(data) # http response
#
#
# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         qs_count = User.objects.all().count()
#         labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         default_items = [qs_count, 23, 2, 3, 12, 2]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)