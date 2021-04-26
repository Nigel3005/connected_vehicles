from django.urls import include, path
from . import views
# from .views import home
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('status', views.status, name='status'),
    path('', views.indexView, name='Home'),
    path('login', LoginView.as_view(), name="Login"),
    path('register', LoginView.as_view(), name="Register"),
]