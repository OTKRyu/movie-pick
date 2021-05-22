from rest_framework import serializers
from .models import Review, Comment
from movies.serializers import MovieAutoSerializer
from accounts.serializers import UserSimpleSerializer

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer()
    movie = MovieAutoSerializer()
    class Meta:
        model = Review
        fields = ['id','title', 'movie', 'created_at', 'user']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    user_like = UserSimpleSerializer(many=True, read_only=True)
    movie = MovieAutoSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'