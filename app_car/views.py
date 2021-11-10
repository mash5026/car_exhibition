from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Car, Company, Agency

# Create your views here.


def home(request):
    return render(request,'app_car/home.html')

def cars(request):
    template_cars = 'app_car/cars.html'
    all_cars = Car.objects.all()
    context = {
        'cars':all_cars
    }
    return render(request, template_cars, context)
