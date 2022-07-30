from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post


# Create your views here.

def blog_list_view(request):
    blogs = Post.objects.all()

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    try:
        all_post_pages = paginator.get_page(page_number)
    except PageNotAnInteger:
        all_post_pages = paginator.get_page(1)
    except EmptyPage:
        all_post_pages = paginator.get_page(paginator.num_pages)

    context = {'all_post_pages': all_post_pages}
    return render(request, template_name='blog/blog_list.html', context=context)


def blog_single_view(request):
    return render(request, template_name='blog/blog_single.html')
