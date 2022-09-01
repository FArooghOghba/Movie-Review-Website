from django.urls import path
from .views import *

from movie.feeds import LatestMoviesFeed

app_name = 'movie'

urlpatterns = [
    path('', movie_list_view, name='list'),
    path('single/<slug:movie_slug>/', movie_single_view, name='single'),

    path('genre/<slug:genre_slug>/', movie_list_view, name='genre'),
    path('topic/<str:topic_name>/', movie_list_view, name='topic'),
    path('search/', movie_search_view, name='search'),
    path('rss/feed/', LatestMoviesFeed()),
]
