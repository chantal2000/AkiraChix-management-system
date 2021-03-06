# Generated by Django 3.2.4 on 2021-08-20 10:02

import datetime
from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=12)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime.now)),
                ('trainer_id', models.PositiveSmallIntegerField(default=1)),
                ('national_Id', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('profile_image', models.ImageField(upload_to='')),
                ('course_name', models.CharField(max_length=30)),
                ('languages', models.CharField(choices=[('k', 'kinyarwanda'), ('E', 'English'), ('L', 'Luganda'), ('k', 'kiswahili')], max_length=30)),
            ],
        ),
    ]
