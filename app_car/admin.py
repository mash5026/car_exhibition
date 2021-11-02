from django.contrib import admin

from django.contrib import admin
from .models import Car, Company,Agency
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name','year','price')
    list_filter = ('name', 'company','agency','year','price','stock')
    search_fields = ('name', 'company','agency','year','price')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    list_filter = ('name','country')
    search_fields = ('name','country')


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name','code','status','url_site')
    list_filter = ('name','code', 'status')
    search_fields = ('name','code')


