from django import forms
from django.db import models
from django.db.models import fields
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="username", label_suffix="", widget=forms.TextInput(attrs={
        'class':'input100','placeholder':'نام کاربری را وارد نمایید', 'title':''
    }))
    password = forms.CharField(label="password", label_suffix="", widget=forms.PasswordInput(attrs={
        'class':'input100','placeholder':'کلمه عبور را وارد نمایید', 'title':''}))


class ProfileForm(forms.ModelForm):
    # username = forms.CharField(label='نام کاربری')
    # password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput)
    bio = forms.CharField(label='درباره من', required=False)
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email']
        labels={}
        help_texts={'username':"",}
    
    # def clean_username(self):
    #     data = self.cleaned_data["username"]
    #     if len(data) < 5:
    #         self.add_error('username', 'نام کاربری می بایست بیشتر از 5 حرف باشد')
    #     return data
    

