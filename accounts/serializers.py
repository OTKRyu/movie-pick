from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import MovieListSerializer, MovieAutoSerializer
from .models import Rate

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','nickname']

class RateSerializer(serializers.ModelSerializer):
    movie = MovieAutoSerializer(read_only=True)
    user = UserSimpleSerializer(read_only=True)
    rate = serializers.IntegerField(min_value=0, max_value=5)
    class Meta:
        model = Rate
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    movie_to_see = MovieAutoSerializer(many=True)
    rated_movies = MovieAutoSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ['id','username','nickname', 'user_img','movie_to_see', 'rated_movies']