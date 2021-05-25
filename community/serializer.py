from rest_framework import serializers
from .models import Review, Comment
from movies.serializers import MovieAutoSerializer
from accounts.serializers import UserSimpleSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'user','content']

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer()
    movie = MovieAutoSerializer()
    user_like_count = serializers.IntegerField(source='user_like.count',read_only=True)
    class Meta:
        model = Review
        fields = ['id','title', 'movie', 'user', 'updated_at','user_like_count']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    user_like = UserSimpleSerializer(many=True, read_only=True)
    user_like_count = serializers.IntegerField(source='user_like.count',read_only=True)
    movie = MovieAutoSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id','title','user','movie','user_like','user_like_count','comment_set','content','created_at','updated_at']

