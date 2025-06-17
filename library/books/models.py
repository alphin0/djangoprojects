from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField()
    author = models.CharField()
    language = models.CharField()
    pages = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='books_img')