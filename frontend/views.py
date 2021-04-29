from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from api.models import vehicleStatus
from django.contrib.auth.decorators import login_required
from frontend.forms import SignUpForm
from user_profile.tokens import account_activation_token
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login



def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)

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
        return redirect('home')
    else:
        return render(request, 'registration/account-activation-invalid.html')

@login_required()
def account_activation_sendView(request):
    template_name = '../templates/registration/account-activation-send.html'
    return render(request, template_name)

@login_required
def statusView(request):
    template_name = 'status.html'
    vehicleid = request.user.profile.vehicle_id
    vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid)
    args = {'vehicle_statusses': vehicle_statusses, 'vehicleid':vehicleid}
    return render(request, template_name, args)

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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
