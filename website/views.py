from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta

from movie.models import Movie


# Create your views here.

def index_view(request):
    today = timezone.now()
    last_tree_month = today - timedelta(days=90)

    movies = Movie.objects.all()
    upcoming = movies.filter(release_date__gt=today)[:8]
    best_in_library = movies.filter(rating__gte=7.0)[:8]
    released = movies.filter(release_date__range=(last_tree_month, today))[:8]

    context = {
        'upcoming': upcoming,
        'best_in_library': best_in_library,
        'released': released
    }
    return render(request, template_name='website/index.html', context=context)


def blog_list_view(request):
    return render(request, template_name='website/blog_list.html')


def about_view(request):
    return render(request, template_name='website/about.html')


def contact_view(request):
    return render(request, template_name='website/contact.html')
