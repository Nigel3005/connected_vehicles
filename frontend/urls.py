from django.urls import include, path
from . import views
# from .views import home
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.conf.urls import url

urlpatterns = [
    path('status', views.statusView, name='status'),
    path('', views.indexView, name='Home'),
    path('login', LoginView.as_view(), name="Login"),
    path('register', views.registerView, name="Register"),
    path('account_activation_sent', views.account_activation_sentView, name="Register"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activateView, name='Account Activeren'),
]