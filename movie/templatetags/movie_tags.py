from datetime import timedelta

from django import template
from django.db.models import Count
from django.utils import timezone

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


@register.inclusion_tag('movie/theater_slider.html')
def movie_in_theater_slider():
    today = timezone.now()
    last_tree_month = today - timedelta(days=90)

    movies = Movie.objects \
        .prefetch_related('genre', 'rating') \
        .filter(rating__average__gte=7.0) \
        .filter(release_date__range=(last_tree_month, today)) \
        .order_by('-rating__average')[:7]

    return {'movies': movies}


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
