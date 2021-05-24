from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.get_profile),
    path('profile/series/', views.get_or_change_series),
    path('profile/character/', views.change_charactor),
    path('profile/schedule/', views.get_schedule),
    path('<int:movie_pk>/movie_to_see/', views.toggle_movie_to_see),
    path('<int:movie_pk>/rated_movie/', views.change_rated_movie),
]
