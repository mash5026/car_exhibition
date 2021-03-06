# Generated by Django 3.2.9 on 2021-12-02 08:37

import accounts.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='درباره من')),
                ('phone', models.CharField(blank=True, help_text='شماره همراه با صفر وارد شود', max_length=11, null=True, verbose_name='شماره همراه')),
                ('avatar', models.ImageField(upload_to=accounts.utils.get_image_path, validators=[accounts.utils.image_size], verbose_name='تصویر کاربر')),
                ('gender', models.CharField(choices=[('m', 'مرد'), ('f', 'بانو'), ('o', 'دیگر')], max_length=10, verbose_name='جنسیت')),
                ('nc', models.CharField(max_length=10, null=True, verbose_name='کدملی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]
