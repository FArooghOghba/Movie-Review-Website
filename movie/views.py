from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from movie.models import Movie


# Create your views here.

def movie_list_view(request):
    movies = Movie.objects.prefetch_related('genre').all()
    # rating = Movie.objects.filter()
    # rating = AbstractBaseRating.objects.filter(average__gte=7.0)
    # print(rating)

    paginator = Paginator(movies, 6)
    page_number = request.GET.get('page')
    try:
        all_movie_pages = paginator.get_page(page_number)
    except PageNotAnInteger:
        all_movie_pages = paginator.get_page(1)
    except EmptyPage:
        all_movie_pages = paginator.get_page(paginator.num_pages)

    context = {'all_movie_pages': all_movie_pages}
    return render(request, template_name='movie/movie_list.html', context=context)


def movie_single_view(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)

    context = {'movie': movie}
    return render(request, template_name='movie/movie_single.html', context=context)
