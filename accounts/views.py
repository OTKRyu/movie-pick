from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer, RateSerializer
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
def change_series(request):
    if request.method == 'GET':
        series = Series.objects.get(name=request.user.series)
        movies = series.movie_set.all()
        result = []
        for movie in movies:
            if request.user.rated_movies.filter(pk=movie.pk).exists():
                continue
            else:
                serializer = MovieListSerializer(instance=movie)
                result.append(serializer.data)
        return Response(result, status=status.HTTP_200_OK)
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
                    'content': "당신은 슈트를 즐겨입습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 부자입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 힘이 셉니까?",
                },
                {
                    'is_question': True,
                    'content': "희소자원을 많이 가지고 있습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 애국심을 가지고 있습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신의 사회적 지위는 높은 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 마법을 믿는 편입니까?",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '블랙팬서',
                        'img_url' : 'http://localhost:8000/static/black_panther.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '아이언맨',
                        'img_url' : 'http://localhost:8000/static/iron_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '캡틴 아메리카',
                        'img_url' : 'http://localhost:8000/static/captiain_america.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '앤트맨',
                        'img_url' : 'http://localhost:8000/static/antman.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '토르',
                        'img_url' : 'http://localhost:8000/static/thor.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '헐크',
                        'img_url' : 'http://localhost:8000/static/hulk.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '닥터 스트레인지',
                        'img_url' : 'http://localhost:8000/static/dr_strange.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '블랙 위도우',
                        'img_url' : 'http://localhost:8000/static/black_widow.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "사람들이 당신의 과거에 대해 잘 아는 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 인간을 초월한 힘을 가지고 있습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 성별은 남자입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 하늘보다 물 속을 더 좋아합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신의 본명은 당신의 별명만큼이나 유명합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 가솔린, 화약, 다이너마이트를 좋아합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 양갈래 머리를 한 적이 있습니까?",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '아쿠아맨',
                        'img_url' : 'http://localhost:8000/static/aqua_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '슈퍼맨',
                        'img_url' : 'http://localhost:8000/static/aqua_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '배트맨',
                        'img_url' : 'http://localhost:8000/static/bat_man.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '조커',
                        'img_url' : 'http://localhost:8000/static/jocker.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '조커(다크나이트)',
                        'img_url' : 'http://localhost:8000/static/jocker_darknight.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '샤잠',
                        'img_url' : 'http://localhost:8000/static/shazam.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '할리퀸',
                        'img_url' : 'http://localhost:8000/static/harley_quinn.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '원더우먼',
                        'img_url' : 'http://localhost:8000/static/wonder_woman.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "당신은 그리핀도르입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 로맨스를 좋아합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 세계정복을 꿈꾼 적이 있습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 모범생인 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신의 통장잔고는 넉넉합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신의 콧대는 높은 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 말이 많은 편입니까?",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '헤르미온느',
                        'img_url' : 'http://localhost:8000/static/hermione.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '론위즐리',
                        'img_url' : 'http://localhost:8000/static/ron.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '해리포터',
                        'img_url' : 'http://localhost:8000/static/harry.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '도비',
                        'img_url' : 'http://localhost:8000/static/dobby.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '덤블도어',
                        'img_url' : 'http://localhost:8000/static/dumbledore.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '볼드모트',
                        'img_url' : 'http://localhost:8000/static/voldemort.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '말포이',
                        'img_url' : 'http://localhost:8000/static/malfoy.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '스네이프',
                        'img_url' : 'http://localhost:8000/static/snape.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "당신은 반려동물을 기르고 싶나요?",
                },
                {
                    'is_question': True,
                    'content': "당신은 기계에 친숙합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 빌런이 되고 싶다고 생각한 적 있습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 키가 큰 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 털이 많은 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 대장 노릇을 좋아합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 노력형입니까?",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': 'C3-PO',
                        'img_url' : 'http://localhost:8000/static/c3po.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': 'R2D2',
                        'img_url' : 'http://localhost:8000/static/r2d2.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '츄바카',
                        'img_url' : 'http://localhost:8000/static/chewbacca.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '요다',
                        'img_url' : 'http://localhost:8000/static/toda.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '다스베이더',
                        'img_url' : 'http://localhost:8000/static/darth_vader.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '스톰트루퍼',
                        'img_url' : 'http://localhost:8000/static/stormtrooper.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '루크',
                        'img_url' : 'http://localhost:8000/static/luke.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '레아 공주',
                        'img_url' : 'http://localhost:8000/static/princess.jpg'
                    },
                },
            ],
            [
                None,
                {
                    'is_question': True,
                    'content': "당신은 키가 커지고 싶습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 소유욕이 강한 편입니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 멋진 수염을 가지고 있습니까?",
                },
                {
                    'is_question': True,
                    'content': "혹시 탈모...?",
                },
                {
                    'is_question': True,
                    'content': "당신은 여행을 좋아합니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 결혼을 하셨습니까?",
                },
                {
                    'is_question': True,
                    'content': "당신은 큰 눈을 가졌습니까?",
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '골룸',
                        'img_url' : 'http://localhost:8000/static/gollum.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '프로도',
                        'img_url' : 'http://localhost:8000/static/frodo.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '빌보',
                        'img_url' : 'http://localhost:8000/static/bilbo.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '샘',
                        'img_url' : 'http://localhost:8000/static/sam.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '아라곤',
                        'img_url' : 'http://localhost:8000/static/aragorn.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '간달프',
                        'img_url' : 'http://localhost:8000/static/gandalf.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '사우론',
                        'img_url' : 'http://localhost:8000/static/sauron.jpg'
                    },
                },
                {
                    'is_question': False,
                    'character': {
                        'name': '레골라스',
                        'img_url' : 'http://localhost:8000/static/legolas.jpg'
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
    return Response({'detail':'success'}, status=status.HTTP_202_ACCEPTED)


def get_schedule(request):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
@authentication_classes([JSONWebTokenAuthentication,])
def toggle_movie_to_see(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.movie_to_see.filter(pk=movie_pk).exists():
        request.user.movie_to_see.remove(movie)
        return Response({'detail':'successfully removed'},status=status.HTTP_204_NO_CONTENT)
    else:
        request.user.movie_to_see.add(movie)
        return Response({'detail':'successfully added'}, status=status.HTTP_201_CREATED)

def change_rated_movie(request, movie_pk):
    pass


