# Generated by Django 3.2.9 on 2021-11-09 11:29

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0003_car_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ثبت'),
        ),
    ]
