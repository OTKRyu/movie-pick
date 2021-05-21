from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auto/<str:keyword>/', views.auto),
    path('search/<str:keyword>/', views.search),
    path('<int:movie_pk>/', views.detail),
]