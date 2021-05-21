from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
def change_series(request):
    pass

def change_charactor(request):
    pass

def get_schedule(request):
    pass

def toggle_movie_to_see(request, movie_pk):
    pass

def change_rated_movie(request, movie_pk):
    pass


