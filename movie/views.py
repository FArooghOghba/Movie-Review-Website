from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from movie.models import Movie


# Create your views here.

def movie_list_view(request):
    movies = Movie.objects.all()

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
