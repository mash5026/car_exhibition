from django.urls import path
from . import views

app_name = 'app_car'

urlpatterns = [
    path('', views.home, name="home"),
    path('cars/', views.cars, name='cars')
]