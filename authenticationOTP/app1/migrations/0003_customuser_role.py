# Generated by Django 5.2 on 2025-06-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customuser_is_verified_customuser_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='', max_length=20),
        ),
    ]
