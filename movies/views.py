from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Movie
from .serializers import MovieListSerializer,MovieSerializer, MovieAutoSerializer
from accounts.models import Rate
from accounts.serializers import RateSerializer
from django.core.paginator import Paginator
from django.db.models import Avg
# Create your views here.
import random
@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def index(request):
    nums = [57, 15, 59, 42, 31, 5, 14, 48, 0, 41, 3, 8, 52, 46, 20, 9, 58, 17, 22, 21, 6, 1, 26, 32, 18, 10, 24, 23, 30, 44, 43, 28, 13, 33, 50, 54, 55, 40, 19, 45, 27, 53, 35, 47, 
11, 12, 60, 37, 4, 2, 56, 36, 29, 39, 16, 51, 7, 49, 25, 34, 38]
    movies = Movie.objects.all()    
    new_movies = [movies[nums[i]] for i in range(61)]
    page_number = int(request.query_params.dict()['page'])
    if (page_number-1)*10 < len(movies):
        page_obj = new_movies[(page_number-1)*10:(page_number)*10]
        serializer = MovieListSerializer(instance=page_obj, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'there is no such page'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def auto(request, keyword):
    keyword = keyword
    movies = Movie.objects.filter(title__contains=keyword)
    serializer = MovieAutoSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def search(request, keyword):
    keyword = keyword
    movies = Movie.objects.filter(title__contains=keyword)
    serializer = MovieListSerializer(instance=movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_serializer = MovieSerializer(instance=movie)
    avg_rate = Rate.objects.filter(movie=movie).aggregate(Avg('rate'))
    rates = Rate.objects.filter(movie=movie)
    rates_serializer = RateSerializer(instance=rates, many=True)
    return Response({'movie':movie_serializer.data, 'rates':rates_serializer.data, 'avg_rate':round(avg_rate['rate__avg'],1)}, status=status.HTTP_200_OK)