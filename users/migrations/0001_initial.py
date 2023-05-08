# Generated by Django 4.2.1 on 2023-05-08 21:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='유저 아이디')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(220)], verbose_name='나이')),
                ('introduction', models.TextField(verbose_name='자기 소개')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('followings', models.ManyToManyField(blank=True, related_name='followers', to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
