from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from api.models import vehicleStatus
from frontend.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render



def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def statusView(request):
    if not request.user.is_anonymous:
        vehicleid = request.user.profile.vehicle_id
        if vehicleid != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid).order_by('time').reverse()
            args = {'page':'status.html', 'vehicle_statusses': vehicle_statusses, 'vehicleid': vehicleid}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'status.html', 'vehicle_statusses': None, 'vehicleid': vehicleid}
            return render(request, 'default.html', args)
    else:
        args = {'page': 'status.html', 'vehicle_statusses': None}
        return render(request, 'default.html', args)

def logboekView(request):
    if not request.user.is_anonymous:
        vehicleid = request.user.profile.vehicle_id
        if vehicleid != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid).order_by('time').reverse()
            args = {'page':'logboek.html', 'vehicle_statusses': vehicle_statusses, 'vehicleid': vehicleid}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'logboek.html', 'vehicle_statusses': None, 'vehicleid': vehicleid}
            return render(request, 'default.html', args)
    else:
        args = {'page': 'logboek.html', 'vehicle_statusses': None}
        return render(request, 'default.html', args)

def profielView(request):
    if not request.user.is_anonymous:
        vehicleid = request.user.profile.vehicle_id
        if vehicleid != None:
            vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid).order_by('time').reverse()
            args = {'page': 'profiel.html', 'vehicle_statusses': vehicle_statusses, 'vehicleid': vehicleid}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'profiel.html', 'vehicle_statusses': None, 'vehicleid': vehicleid}
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
    return redirect('Data-Analytics')