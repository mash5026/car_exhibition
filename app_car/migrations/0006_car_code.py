# Generated by Django 3.2.9 on 2021-11-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0005_car_descript'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='code',
            field=models.PositiveSmallIntegerField(null=True, unique=True, verbose_name='کد خودرو'),
        ),
    ]
