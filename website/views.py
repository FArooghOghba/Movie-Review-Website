from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from datetime import timedelta
from itertools import chain

from movie.models import Movie
from blog.models import Post

from website.forms import ContactForm, NewsletterForm


# Create your views here.

def index_view(request):
    today = timezone.now()
    last_tree_month = today - timedelta(days=90)

    movies = Movie.objects.prefetch_related('genre', 'rating').all()
    upcoming = movies.filter(release_date__gt=today)[:8]
    best_in_library = movies.filter(rating__average__gte=7.0).order_by('-rating__average')[:8]
    released = movies.filter(release_date__range=(last_tree_month, today))[:8]

    context = {
        'upcoming': upcoming,
        'best_in_library': best_in_library,
        'released': released
    }
    return render(request, template_name='website/index.html', context=context)


def about_view(request):
    return render(request, template_name='website/about.html')


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()

            print(contact_form.errors.as_data())
            messages.success(request, 'Your request sent Successfully.')
        else:
            print(contact_form.errors.as_data())
            messages.error(request, 'Something is wrong.')

    contact_form = ContactForm()
    context = {'contact_form': contact_form}
    return render(request, template_name='website/contact.html', context=context)


def search_view(request):
    if request.method == 'GET':
        if search := request.GET.get('search'):
            category = request.GET.get('category')

            if category == 'blog':
                query_set = Post.objects.filter(
                    Q(title__icontains=search) |
                    Q(content__icontains=search) |
                    Q(tag__name__icontains=search)
                ).distinct()
                template = 'blog/blog_list.html'
            elif category == 'movie':
                query_set = Movie.objects.filter(
                    title__icontains=search
                )
                template = 'movie/movie_list.html'
            elif category == 'all':
                movies = Movie.objects.filter(
                    title__icontains=search
                )
                posts = Post.objects.filter(
                    Q(title__icontains=search) |
                    Q(content__icontains=search) |
                    Q(tag__name__icontains=search)
                ).distinct()
                query_set = list(chain(movies, posts))
                template = 'all_category_search.html'
            else:
                return redirect('website:home_page')

            paginator = Paginator(query_set, 3)
            page_number = request.GET.get('page')
            try:
                all_search_pages = paginator.get_page(page_number)
            except PageNotAnInteger:
                all_search_pages = paginator.get_page(1)
            except EmptyPage:
                all_search_pages = paginator.get_page(paginator.num_pages)

            if not isinstance(page_number, int):
                page_number = 1
            if page_number > paginator.num_pages:
                page_number = paginator.num_pages

            page_range = paginator.get_elided_page_range(
                number=page_number,
                on_ends=1,
                on_each_side=1
            )

            context = {
                'all_pages': all_search_pages,
                'page_range': page_range,
            }
            return render(request, template_name=template, context=context)

    return redirect('website:home_page')


def newsletter_view(request):
    page_url = ''

    if request.method == 'POST':
        page_url = request.POST.get('page_url')

        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            print(newsletter_form.errors.as_data())
            messages.success(request, 'Your request sent Successfully.')
        else:
            messages.error(request, 'Something is wrong.')
            print(newsletter_form.errors.as_data())

    return redirect(page_url)

