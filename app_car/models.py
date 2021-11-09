from django.db import models
from .utils import path_car,LIST_STATUS,OFFICIAL, validat_image
from django.utils.text import slugify
from django_jalali.db import models as jmodels
from django.utils.safestring import mark_safe

# Create your models here.

class Car(models.Model):
    slug = models.SlugField(verbose_name="پیوند یکتا", null=True, blank=True, allow_unicode=True)
    name = models.CharField(max_length=30, verbose_name="نام خودرو", null=True)
    company = models.ForeignKey("Company", verbose_name="نام برند", on_delete=models.SET_NULL, null=True, blank=True,\
    related_name='cars')
    agency = models.ForeignKey("Agency", verbose_name="نام نمایندگی", on_delete=models.CASCADE,\
    related_name='cars')
    created_at = jmodels.jDateTimeField(verbose_name="تاریخ ثبت",auto_now_add=True, null=True, blank=True )
    year = models.PositiveSmallIntegerField(verbose_name="سال تولید", null=True)
    price = models.PositiveBigIntegerField(verbose_name="قیمت", null=True)
    stock = models.BooleanField(verbose_name="موجود", default=True ,help_text="در صورت موجود بودن علامت کنار آن قابل مشاهده است")
    image = models.ImageField(verbose_name="تصویر خودرو", upload_to =path_car, validators=[validat_image])

    def save(self,*args,**kwrags):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args,**kwrags)
    
    def get_date(self):
        return self.created_at.strftime('در ساعت %H:%m و در تاریخ %Y/%m/%d')
    get_date.short_description="تاریخ ثبت"

    def get_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" alt="{self.name}" width="150" height="100">')
        else:
            return mark_safe('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsNGGjrfSqqv8UjL18xS4YypbK-q7po_8oVQ&usqp=CAU" width="100" height="100">')
    get_image.short_description = 'عکس خودرو'

    class Meta:
        verbose_name = "نام خودرو"
        verbose_name_plural = "نام خودروها"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام برند", null=True)
    country = models.CharField(max_length=30, verbose_name="نام کشور تولید کننده", null=True)
    introduction = models.TextField(verbose_name="معرفی برند" ,null=True, blank=True)


    class Meta:
        verbose_name = "نام برند"
        verbose_name_plural = "نام  برندها"

    def __str__(self):
        return self.name


class Agency(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام نمایندگی", null=True)
    code = models.CharField(max_length=10, verbose_name="کد نمایندگی", null=True)
    phone = models.CharField(max_length=11, verbose_name="شماره تماس", null=True)
    status = models.CharField(max_length=10, choices=LIST_STATUS, default=OFFICIAL)
    address = models.TextField(null=True)
    url_site = models.URLField()


    class Meta:
        verbose_name = "نام نمایندگی"
        verbose_name_plural = "نام نمایندگی ها"

    def __str__(self):
        return self.name

