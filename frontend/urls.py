from django.urls import path
from . import views

urlpatterns = [
    path('status', views.statusView, name='status'),
    path('', views.indexView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('register', views.registerView, name="Register"),
    path('account-activation-send', views.account_activation_sendView, name="account activation send"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activateView, name='activate'),
]