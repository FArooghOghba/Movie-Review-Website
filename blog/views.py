from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import Post, Comment
from .forms import CommentForm


# Create your views here.

def blog_list_view(request, **kwargs):
    all_post = Post.objects.filter(
        published_date__lte=timezone.now(),
        status=True
    )

    if kwargs.get('tag_slug') is not None:
        all_post = all_post.filter(tag__slug=kwargs['tag_slug'])
    if kwargs.get('cat_slug') is not None:
        all_post = all_post.filter(categories__slug=kwargs['cat_slug'])

    page_number = request.GET.get('page', 1)
    paginator = Paginator(all_post, 3)

    try:
        all_post_pages = paginator.get_page(page_number)
    except PageNotAnInteger:
        all_post_pages = paginator.get_page(1)
    except EmptyPage:
        all_post_pages = paginator.get_page(paginator.num_pages)

    page_range = paginator.get_elided_page_range(
        number=page_number,
        on_ends=1,
        on_each_side=1
    )

    context = {
        'all_pages': all_post_pages,
        'page_range': page_range
    }
    return render(request, template_name='blog/blog_list.html', context=context)


def blog_single_view(request, post_slug):
    post = get_object_or_404(
        Post,
        slug=post_slug,
        published_date__lte=timezone.now(),
        status=True
    )

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if not request.user.is_authenticated:
            messages.warning(request, 'You first must Log in.')

        elif comment_form.is_valid():
            new_comment = comment_form.save()

            messages.success(request, 'Your comment submitted Successfully.')
            return redirect(f'{post.get_absolute_url()}#{new_comment}')
        else:
            print(comment_form.errors.as_data())
            messages.error(request, 'Something is wrong.')
            return redirect(post.get_absolute_url())

    context = {
        'post': post,
    }
    return render(request, template_name='blog/blog_single.html', context=context)


def blog_reply_comment_view(request):
    if request.method == 'POST':
        reply_comment_form = CommentForm(data=request.POST)

        post_url = request.POST.get('post_url')

        if not request.user.is_authenticated:
            messages.warning(request, 'You first must Log in.')

        elif reply_comment_form.is_valid():
            parent = request.POST.get('parent')
            new_reply_comment = reply_comment_form.save(commit=False)

            new_reply_comment.parent = Comment(id=parent)
            new_reply_comment.save()

            messages.success(request, 'Your Reply sent Successfully.')
            return redirect(f'{post_url}#{new_reply_comment.id}')
        else:
            print(reply_comment_form.errors.as_data())
            messages.error(request, 'Something is wrong.')
            return redirect(post_url)

    return redirect('/')


def blog_like_post_view(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user

        try:
            if not post.like.filter(id=user.id).exists():
                post.like.add(user)
                post.save()
            else:
                post.like.remove(user)
                post.save()

            context = {'post': post}
            return render(request, 'blog/blog_like_post.html', context=context)

        except TypeError:
            context = {'post': post}
            return render(request, 'blog/blog_like_post.html', context=context)

    return redirect('blog:list')


def blog_search_view(request):
    if request.method == 'GET':
        if search := request.GET.get('s'):
            posts = Post.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(tag__name__icontains=search)
            ).distinct()

            page_number = request.GET.get('page', 1)
            paginator = Paginator(posts, 3)

            try:
                all_post_pages = paginator.get_page(page_number)
            except PageNotAnInteger:
                all_post_pages = paginator.get_page(1)
            except EmptyPage:
                all_post_pages = paginator.get_page(paginator.num_pages)

            page_range = paginator.get_elided_page_range(
                number=page_number,
                on_ends=1,
                on_each_side=1
            )

            context = {
                'all_pages': all_post_pages,
                'page_range': page_range
            }
            return render(request, template_name='blog/blog_list.html', context=context)

    return redirect('blog:list')
