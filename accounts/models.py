from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Series
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    user_img = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)
    movie_to_see = models.ManyToManyField(Movie, 'users_will_see')
    rated_movies = models.ManyToManyField(Movie, related_name='user_rates',through='Rate')
    

    def __str__(self):
        return self.username


class Rate(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_to_rate')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_to_rate')
    rate = models.IntegerField()
    comment = models.CharField(max_length=50)
