from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

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


def blog_single_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {'post': post}
    return render(request, template_name='blog/blog_single.html', context=context)


def blog_search_view(request):
    if request.method == 'GET':
        if search := request.GET.get('search'):
            posts = Post.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

            paginator = Paginator(posts, 3)
            page_number = request.GET.get('page')
            try:
                all_post_pages = paginator.get_page(page_number)
            except PageNotAnInteger:
                all_post_pages = paginator.get_page(1)
            except EmptyPage:
                all_post_pages = paginator.get_page(paginator.num_pages)

            context = {'all_pages': all_post_pages}
            return render(request, template_name='blog/blog_list.html', context=context)

    return redirect('blog:list')
