from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Car, Company, Agency
import random
from django.db.models import Count

# Create your views here.


def home(request):
    return render(request,'app_car/home.html')

def cars(request):
    template_cars = 'app_car/cars.html'
    all_cars = Car.objects.all().order_by('-price')
    context = {
        'cars':all_cars
    }
    return render(request, template_cars, context)

def details(request,slug):
    car = get_object_or_404(Car, slug=slug)
    context = {
        "car":car
    }
    return render(request, 'app_car/details.html', context)

def details_id(request,id):
    car = get_object_or_404(Car, code=id)
    status = car.stock
    context = {
        "car":car, "status":status
    }
    return render(request, 'app_car/details.html', context)

def random_cars(request):
    nums = Car.objects.all().aggregate(numbers = Count('id'))
    print(nums)
    ran = (random.randint(0, nums['numbers']))-1
    my_car = get_object_or_404(Car, id=ran)
    context = {
        "my_car":my_car
    }
    return render(request, 'app_car/random_cars.html', context)
