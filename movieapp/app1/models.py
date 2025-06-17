from django.db import models

# Create your models here.

class Movie(models.Model):         #parent class model class in build
    movie_name=models.CharField(max_length=30)
    description=models.TextField()
    director_name=models.CharField()
    language=models.CharField()
    year=models.IntegerField()
    image = models.ImageField(upload_to='movie_img')