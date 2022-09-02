from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.utils import timezone

from datetime import timedelta

from movie.models import Movie
from blog.models import Post


# Create your views here.

def movie_list_view(request, **kwargs):
    today = timezone.now()
    last_tree_month = today - timedelta(days=90)
    movies = Movie.objects \
        .prefetch_related('genre', 'rating') \
        .order_by('-rating__average')

    if kwargs.get('genre_slug') is not None:
        movies = movies.filter(genre__slug=kwargs['genre_slug'])
    elif kwargs.get('topic_name') is not None:
        if kwargs.get('topic_name') == 'fan_favorite':
            movies = movies.filter(rating__average__gte=7.0) \
                .order_by('-rating__average')
        elif kwargs.get('topic_name') == 'upcoming':
            movies = movies.filter(release_date__gt=today)
        elif kwargs.get('topic_name') == 'released':
            movies = movies.filter(release_date__range=(last_tree_month, today))

    paginator = Paginator(movies, per_page=6)
    page_number = request.GET.get('page', 1)

    try:
        all_movie_pages = paginator.get_page(page_number)
    except PageNotAnInteger:
        all_movie_pages = paginator.get_page(1)
    except EmptyPage:
        all_movie_pages = paginator.get_page(paginator.num_pages)

    page_range = paginator.get_elided_page_range(
        number=page_number,
        on_ends=1,
        on_each_side=1
    )

    context = {
        'all_pages': all_movie_pages,
        'page_range': page_range
    }
    return render(request, template_name='movie/movie_list.html', context=context)


def movie_single_view(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    posts = Post.objects.filter(
        Q(title__icontains=movie.title) |
        Q(content__icontains=movie.title)
    )

    context = {
        'movie': movie,
        'posts': posts
    }
    return render(request, template_name='movie/movie_single.html', context=context)


def movie_search_view(request):
    if request.method == 'GET':
        if search := request.GET.get('search'):

            movies = Movie.objects.filter(title__icontains=search)

            paginator = Paginator(movies, 6)
            page_number = request.GET.get('page')
            try:
                all_movie_pages = paginator.get_page(page_number)
            except PageNotAnInteger:
                all_movie_pages = paginator.get_page(1)
            except EmptyPage:
                all_movie_pages = paginator.get_page(paginator.num_pages)

            context = {'all_pages': all_movie_pages}
            return render(request, template_name='movie/movie_list.html', context=context)

    return redirect('movie:list')
