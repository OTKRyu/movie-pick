from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Series
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    user_img = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    movie_to_see = models.ManyToManyField(Movie, 'users_will_see')
    rated_movies = models.ManyToManyField(Movie,'user_rates',through='Rates')

    
