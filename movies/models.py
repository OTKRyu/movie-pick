from django.db import models


# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    runtiem = models.IntegerField()
    age_rate = models.IntegerField()
    main_actor = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    release_year = models.IntegerField()
    overview = models.TextField()
    later = models.ManyToManyField('self', related_name='earlier')
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

class Character(models.Model):
    name = models.CharField(max_length=20)
    img_path = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

