from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', movie_list_view, name='list'),
    path('single/<slug:movie_slug>/', movie_single_view, name='single'),

    path('search/', movie_search_view, name='search')
]
