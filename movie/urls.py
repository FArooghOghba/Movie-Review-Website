from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', movie_list_view, name='list'),
    path('<int:movie_id>/', movie_single_view, name='single'),
]
