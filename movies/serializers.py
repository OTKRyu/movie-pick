from rest_framework import serializers
from .models import Movie, Series


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields ='__all__'

class MovieListSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    class Meta:
        model = Movie
        fields = ['id','title', 'poster_path','overview', 'series'] 
    
class MovieSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    class Meta:
        model = Movie
        exclude = ['later',]

class MovieAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title',]



