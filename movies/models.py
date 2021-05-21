from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    runtiem = models.IntegerField()
    limit_age = models.IntegerField()
    main_actor = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    release_year = models.IntegerField()
    overview = models.TextField()

class Series(models.Model):
    name = models.CharField(max_length=50)
    
class Character(models.Model):
    name = models.CharField(max_length=20)
    img_path = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

class Rates(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.CharField(max_length=50)
