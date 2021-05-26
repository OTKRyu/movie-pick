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

@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page_number = int(request.query_params.dict()['page'])
    page_obj = paginator.get_page(page_number)
    serializer = MovieListSerializer(instance=page_obj, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

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
    return Response({'movie':movie_serializer.data, 'rates':rates_serializer.data, 'avg_rate':avg_rate}, status=status.HTTP_200_OK)