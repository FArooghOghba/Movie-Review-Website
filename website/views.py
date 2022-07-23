from django.shortcuts import render
from django.utils import timezone

from movie.models import Movie


# Create your views here.

def index_view(request):
    movies = Movie.objects.filter(release_date__gt=timezone.now())

    context = {'movies': movies}
    return render(request, template_name='website/index.html', context=context)


def blog_list_view(request):
    return render(request, template_name='website/blog_list.html')


def about_view(request):
    return render(request, template_name='website/about.html')


def contact_view(request):
    return render(request, template_name='website/contact.html')
