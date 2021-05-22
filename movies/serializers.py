from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title', 'poster_path','overview'] 
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['later',]

class MovieAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title',]