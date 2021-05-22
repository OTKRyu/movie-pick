from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Comment
from .serializer import CommentSerializer, ReviewListSerializer, ReviewSerializer


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
        reviews = Review.objects.order_by('-updated_at')
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
    review = get_object_or_404(Review, pk=review_pk)
    if review.user_like.filter(pk=request.user.pk).exists():
        review.user_like.remove(request.user)
        return Response({'detail':'succes'}, status=status.HTTP_204_NO_CONTENT)
    else:
        review.user_like.add(request.user)
        return Response({'detail':'succes'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def update_or_delete_comment(request, review_pk, comment_pk):
    if request.method == 'PUT':
        review = get_object_or_404(Review, pk=review_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, review=review)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'detail':'you are not authorized'},status=status.HTTP_401_UNAUTHORIZED)
    else:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
            return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail':'you are not authorized'},status=status.HTTP_401_UNAUTHORIZED)

