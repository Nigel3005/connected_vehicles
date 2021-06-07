from django.urls import path, include


from . import views

urlpatterns = [
    path('data-analytics', views.DataAnalyticsView, name='Data-Analytics'),
]
