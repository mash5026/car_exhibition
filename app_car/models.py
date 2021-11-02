from django.db import models
from .utils import path_car,LIST_STATUS,OFFICIAL, validat_image

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام خودرو", null=True)
    company = models.ForeignKey("Company", verbose_name="نام برند", on_delete=models.SET_NULL, null=True, blank=True,\
    related_name='cars')
    agency = models.ForeignKey("Agency", verbose_name="نام نمایندگی", on_delete=models.CASCADE,\
    related_name='cars')
    year = models.PositiveSmallIntegerField(verbose_name="سال تولید", null=True)
    price = models.PositiveBigIntegerField(verbose_name="قیمت", null=True)
    stock = models.BooleanField(verbose_name="موجود", default=True ,help_text="در صورت موجود بودن علامت کنار آن قابل مشاهده است")
    image = models.ImageField(verbose_name="تصویر خودرو", upload_to =path_car, validators=[validat_image])


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

