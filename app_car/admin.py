from django.contrib import admin
from django.contrib import admin
from .models import Car, Company,Agency
from django.contrib import messages
from django.db import models


# Register your models here.
class CarInlineCompany(admin.TabularInline):
    model = Car
    extra = 0


class CarInlineAgency(admin.TabularInline):
    model = Car
    extra = 2


@admin.action(description="ناموجود کردن ماشین ها")
def make_unavailable_car(modeladmin,request,queryset):
    unavailable = queryset.update(stock=False)
    messages.success(request,f"{unavailable} ماشین ناموجود گردید")

@admin.action(description="موجود کردن ماشین ها")
def make_available_car(modeladmin,request,queryset):
    available = queryset.update(stock=True)
    messages.success(request,f"{available} ماشین به حالت موجود تغییر یافت.")

@admin.action(description="افزایش قیمت به میزان 20درصد")
def increase_price(modeladmin,request,queryset):
    all_price = list(queryset.values_list('price'))
    all_cars = queryset.all()
    numbers = queryset.count()
    new_price = list(map(lambda x: x[0]*1.2, all_price))
    for i in range(len(new_price)):
        my_car = all_cars[i]
        my_car.price = new_price[i]
        my_car.save()
    messages.success(request, f"{numbers} قیمت به روز رسانی گردید.")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('get_image','name','year','price','stock','company','get_date')
    list_filter = ('name', 'company','agency','year','price','stock')
    search_fields = ('name','company__name','year','price')
    actions = (make_unavailable_car,make_available_car,increase_price)
    list_display_links = ('name', 'company')
    list_per_page = 100
    sortable_by = ('name', 'company')
    list_editable = ('price','year')
    ordering = ('-year',)
    # readonly_fields = ('agency',)

    # def get_date(self,obj):
    #     return obj.created_at.strftime('در ساعت %H:%m و در تاریخ %Y/%m/%d')
    # get_date.short_description = "تاریخ ایجاد"


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    list_filter = ('name','country')
    search_fields = ('name','country')
    inlines = (CarInlineCompany,)
    

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name','code','status','url_site')
    list_filter = ('name','code', 'status')
    search_fields = ('name','code')
    inlines = (CarInlineAgency,)
    


