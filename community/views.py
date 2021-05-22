from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Review, Comment
from .serializer import ReviewListSerializer, ReviewSerializer


@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def get_top5(request):
    pass

@api_view(['GET','POST'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def index(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by('-created_at')
        paginator = Paginator(reviews, 10)

        page_number = request.data.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = ReviewListSerializer(instance=page_obj, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)        
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def review_detail(request, review_pk):
    if request.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(instance=review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='PUT':
        review = get_object_or_404(Review, pk=review_pk)
        if review.user == request.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'detail':'you are not authorized'},status=status.HTTP_401_UNAUTHORIZED)
    else:
        review = get_object_or_404(Review, pk=review_pk)
        if review.user == request.user:
            review.delete()
            return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail':'you are not authorized'},status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def review_like(request, review_pk):
    pass

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def create_comment(request, review_pk):
    pass

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def update_or_delete_comment(request, review_pk, comment_pk):
    pass

