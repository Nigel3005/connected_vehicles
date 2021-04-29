from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from api.models import vehicleStatus
from django.contrib.auth.decorators import login_required
from frontend.forms import SignUpForm, LoginForm
from user_profile.tokens import account_activation_token
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth import authenticate


def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def activateView(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/home')
    else:
        render(request, 'default.html', {'page': 'registration/account-activation-invalid.html'})


def account_activation_sendView(request):
    template_name = '../templates/registration/account-activation-send.html'
    render(request, 'default.html', {'page': template_name})

@login_required
def statusView(request):
    vehicleid = request.user.profile.vehicle_id
    vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid)
    args = {'page':'status.html', 'vehicle_statusses': vehicle_statusses, 'vehicleid':vehicleid}
    render(request, 'default.html', args)

def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your connected vehicles Account'
            message = render_to_string('registration/account-activation-email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('/account-activation-send')
    else:
        form = SignUpForm()
        return render(request, 'default.html', {'page': 'registration/register.html', 'form': form})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.username, password=form.password)
            if user is not None:
                if user.is_active:
                    return redirect('/status')
                else:
                    form = LoginForm
                    return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Account is not activated'})
            else:
                form = LoginForm
                return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Your username and password were incorrect.'})
        else:
            form = LoginForm
            return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Invalid Form'})

    else:
        form = LoginForm
        return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error':None})