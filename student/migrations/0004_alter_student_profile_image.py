# Generated by Django 3.2.4 on 2021-08-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210822_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
