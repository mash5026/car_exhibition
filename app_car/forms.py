from django import forms
from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):

    class Meta:
        model = Car
        exclude = ['slug','code','created_at']


class EditCarForm(ModelForm):

    class Meta:
        model = Car
        exclude = ['slug','code','created_at']