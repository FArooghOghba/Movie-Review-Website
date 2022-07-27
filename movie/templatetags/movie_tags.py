from django import template
from django.db.models import Count

from movie.models import Genre, Movie

register = template.Library()


@register.inclusion_tag('movie/movie_genres.html')
def get_genres_count():
    movies_genres_count = Genre.objects \
        .annotate(movie_count=Count('movie'))

    all_movie_count = Movie.objects.count()

    return {
        'all_movie_count': all_movie_count,
        'movies_genres_count': movies_genres_count
    }


@register.filter
def duration(movie_duration):
    total_seconds = int(movie_duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return f'{hours} hrs {minutes} mins'


@register.filter(name="popularity_percent")
def popularity_percentage(rating):
    result = (rating * 100) / 10
    return round(result)
