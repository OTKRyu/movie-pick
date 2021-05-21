from django.urls import path
from . import views

urlpatterns = [
    path('profile/series/', views.change_series),
    path('profile/character/', views.change_charactor),
    path('profiel/schedule/', views.get_schedule),
]
