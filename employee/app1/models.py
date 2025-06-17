from django.db import models

# Create your models here.

class Employee(models.Model):
    objects = None
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images')
    department_name=models.CharField(max_length=30)
