from django.db import models


# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=50)\
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    runtime = models.IntegerField()
    age_rate = models.IntegerField()
    main_actor = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    release_year = models.IntegerField()
    overview = models.TextField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    later = models.ManyToManyField('self', related_name='earlier')
    

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=20)
    img_path = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

