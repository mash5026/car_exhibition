from django.urls import path
from . import views

app_name = 'app_car'

urlpatterns = [
    path('', views.home, name="home"),
    path('cars/', views.cars, name='cars'),
    path('details/<str:slug>/', views.details, name="details"),
    path('details_id/<int:id>/', views.details_id, name="details_id"),
    path('random-cars/', views.random_cars, name="random"),
]