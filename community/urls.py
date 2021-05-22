from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('top5/', views.get_top5),
    path('<int:review_pk>/', views.review_detail),
    path('<int:review_pk>/like/', views.review_like),
    path('<int:review_pk>/comment/', views.create_comment),
    path('<int:review_pk>/comment/<int:comment_pk>', views.update_or_delete_comment),
]
