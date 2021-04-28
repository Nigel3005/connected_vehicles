from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render
from api.models import vehicleStatus
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from frontend.forms import SignUpForm


def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)

@login_required
def status(request):
    template_name = 'status.html'
    vehicleid = request.user.profile.vehicle_id
    vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid)
    args = {'vehicle_statusses': vehicle_statusses, 'vehicleid':vehicleid}
    return render(request, template_name, args)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})