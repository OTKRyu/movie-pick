from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieListSerializer,MovieSerializer, MovieAutoSerializer
from django.core.paginator import Paginator
# Create your views here.

@api_view(['GET'])
@permission_classes(( AllowAny, ))
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.data.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = MovieListSerializer(instance=page_obj, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes(( AllowAny, ))
def auto(request, keyword):
    keyword = keyword
    movies = Movie.objects.filter(title__contains=keyword)
    serializer = MovieAutoSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes(( AllowAny, ))
def search(request, keyword):
    keyword = keyword
    movies = Movie.objects.filter(title__contains=keyword)
    serializer = MovieListSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes(( AllowAny, ))
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data, status=status.HTTP_200_OK)