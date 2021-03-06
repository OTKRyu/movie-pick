from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer
from .models import Rate
from movies.models import Series, Movie
from movies.serializers import MovieListSerializer

from accounts import serializers
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def get_profile(request):
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def get_or_change_series(request):
    if request.method == 'GET':
        tmp = Rate.objects.filter(user=request.user).values('series').annotate(Avg('rate'))
        series_id = 1
        maximum = 0
        for i in range(len(tmp)):
            if tmp[i]['rate__avg'] > maximum:
                maximum = tmp[i]['rate__avg']
                series_id = tmp[i]['series']
        series = Series.objects.get(pk=series_id)
        request.user.series = series
        request.user.save()
        movies = series.movie_set.all()
        result = []
        for movie in movies:
            if request.user.rated_movies.filter(pk=movie.pk).exists():
                continue
            else:
                result.append(movie)
        if result:
            final_result = []
            for i in range(len(result)):
                serializer = MovieListSerializer(instance=result[i])
                final_result.append(serializer.data)
            return Response(final_result, status=status.HTTP_200_OK)
        else:
            maximum = 0
            idx = 1
            for i in range(movies):
                rate = Rate.objects.filter(movie=movies[i]).aggregate(Avg('rate'))
                if rate > maximum:
                    maximum = rate
                    idx = i
            serializer = MovieListSerializer(instance=movies[idx])
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        datas = request.data
        for i in range(len(datas)):
            movie = Movie.objects.get(id=datas[i]['movie_id'])
            if 0<=datas[i]['rate']<=5:
                request.user.rated_movies.add(movie,through_defaults={'rate':datas[i]['rate'], 'series':movie.series})
        tmp = Rate.objects.filter(user=request.user).values('series').annotate(Avg('rate'))
        series_id = 1
        maximum = 0
        for i in range(len(tmp)):
            if tmp[i]['rate__avg'] > maximum:
                maximum = tmp[i]['rate__avg']
                series_id = tmp[i]['series']
        series = Series.objects.get(pk=series_id)
        request.user.series = series
        request.user.save()
        question_trees = [
            None,
            [
                None,
                {
                    'is_question': True,
                    'content': "????????? ????????? ???????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????? ??????????",
                },
                {
                    'is_question': True,
                    'content': "??????????????? ?????? ????????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ???????????? ????????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????? ?????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ?????? ?????????????",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/black_panther.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/iron_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????? ????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/captiain_america.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/antman.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/thor.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/hulk.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????? ???????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/dr_strange.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????? ?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/black_widow.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "???????????? ????????? ????????? ?????? ??? ?????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????? ?????? ????????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ???????????? ??? ?????? ??? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????? ?????????????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????????, ??????, ????????????????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????? ??? ?????? ?????????????",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/aqua_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/aqua_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/bat_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/jocker.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????(???????????????)',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/jocker_darknight.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/shazam.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/harley_quinn.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/wonder_woman.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "????????? ?????????????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ???????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ??????????????? ?????? ?????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ???????????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ??????????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ?????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????? ?????? ?????????????",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '???????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/hermione.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/ron.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/harry.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/dobby.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/dumbledore.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/voldemort.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/malfoy.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/snape.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "????????? ??????????????? ????????? ??????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ?????? ????????? ????????? ??? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????? ??? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????? ?????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????? ????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ???????????????????",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': 'C3-PO',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/c3po.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': 'R2D2',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/r2d2.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/chewbacca.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/toda.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '???????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/darth_vader.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '???????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/stormtrooper.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/luke.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????? ??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/princess.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "????????? ?????? ????????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ???????????? ?????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ?????? ????????? ????????? ?????????????",
                },
                {
                    'is_question': True,
                    'content': "?????? ??????...?",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ????????? ????????????????",
                },
                {
                    'is_question': True,
                    'content': "????????? ??? ?????? ????????????????",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/gollum.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/frodo.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '??????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/bilbo.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '???',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/sam.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/aragorn.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/gandalf.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '?????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/sauron.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '????????????',
                        'img_url' : 'http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/static/legolas.jpg'
                    },
                },
            ]
        ]
        return Response(question_trees[series_id], status=status.HTTP_202_ACCEPTED)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def change_charactor(request):
    request.user.nickname = request.data['nickname']
    request.user.user_img = request.data['user_img']
    request.user.save()
    return Response({'detail':'successfully changed'}, status=status.HTTP_202_ACCEPTED)

from collections import deque
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def get_schedule(request):
    series_id = request.data.get('series')
    if series_id:
        series = get_object_or_404(Series, pk=series_id)
        movies = request.user.movie_to_see.filter(series=series)
    else:
        movies = request.user.movie_to_see.all()
    times = request.data.get('times')
    check = [0]*len(movies)
    laters = [[] for i in range(len(movies))]
    for i in range(len(movies)):
        movie = movies[i]
        laters[i] = movie.later.all()
        for j in range(len(movies)):
            if movies[j] in laters[i]:
                check[j] += 1
    q = deque()
    for i in range(len(movies)):
        if check[i] == 0:
            q.append(i)
    result = []
    while q:
        c = q.popleft()
        result.append(c)
        for i in range(len(movies)):
            if movies[i] in laters[c]:
                check[i] -= 1
                if check[i] == 0:
                    q.append(i)
    idx = 0
    tidx = 0
    while idx < len(movies) and tidx < len(times):
        if times[tidx].get('time') > movies[result[idx]].runtime:
            if times[tidx].get('movies'):
                serializer = MovieListSerializer(instance=movies[result[idx]])
                times[tidx]['movies'].append(serializer.data)
                times[tidx]['time'] -= movies[result[idx]].runtime
                idx += 1
            else:
                serializer = MovieListSerializer(instance=movies[result[idx]])
                times[tidx]['movies'] = []
                times[tidx]['movies'].append(serializer.data)
                times[tidx]['time'] -= movies[result[idx]].runtime
                idx += 1
        else:
            tidx += 1
    return Response(times, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def toggle_movie_to_see(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.movie_to_see.filter(pk=movie_pk).exists():
        request.user.movie_to_see.remove(movie)
        return Response({'detail':False },status=status.HTTP_204_NO_CONTENT)
    else:
        request.user.movie_to_see.add(movie, through_defaults={'series':movie.series})
        return Response({'detail':True }, status=status.HTTP_201_CREATED)

@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def change_rated_movie(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if Rate.objects.filter(user=request.user, movie=movie).exists():
            rate = Rate.objects.get(user=request.user,movie=movie)
            if 0<=request.data.get('rate')<=5:
                rate.rate = request.data['rate']
                rate.comment = request.data['comment']
                rate.save()
                return Response({'detail':'successfully changed'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'detail':'rate should be in range 0 to 5'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if 0<=request.data.get('rate')<=5:
                request.user.rated_movies.add(movie, through_defaults={'rate':request.data.get('rate'),'comment':request.data.get('comment'),'series':movie.series})
                return Response({'detail':'successfully added'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail':'rate should be in range 0 to 5'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        request.user.rated_movies.remove(movie)
        return Response({'detail': 'successfully removed'}, status=status.HTTP_204_NO_CONTENT)


