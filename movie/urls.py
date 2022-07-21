from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', movie_list_view, name='movie_list')
]
