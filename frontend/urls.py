from django.urls import include, path
from django.conf.urls import url
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
    path('account-activation-send', views.account_activation_sendView, name="Register"),
    path(r'^activate/<uidb64>/<token>/', views.activateView, name='activate'),

]