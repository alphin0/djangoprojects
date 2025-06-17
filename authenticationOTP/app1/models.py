from django.contrib.auth.models import AbstractUser
from django.db import models
from random import randint

# Create your models here.

class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    address=models.TextField(default='')
    role=models.CharField(max_length=20,default='')
    is_verified = models.BooleanField(default=False)  # After verification it will set to true
    otp = models.CharField(max_length=10, null=True, blank=True)  # To store the generated otp in backend table

    def generate_otp(self):
        otp_number = str(randint(1000, 9999)) + str(self.id)
        self.otp = otp_number
        self.save()