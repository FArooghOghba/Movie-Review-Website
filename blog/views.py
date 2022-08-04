from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Post, Comment
from .forms import CommentForm


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

    context = {'all_pages': all_post_pages}
    return render(request, template_name='blog/blog_list.html', context=context)


def blog_single_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save()
            return redirect(f'{post.get_absolute_url()}#{new_comment}')
        else:
            print(comment_form.errors.as_data())
            return redirect(post.get_absolute_url())

    context = {
        'post': post,
    }
    return render(request, template_name='blog/blog_single.html', context=context)


def blog_reply_comment_view(request):
    if request.method == 'POST':
        reply_comment_form = CommentForm(data=request.POST)

        post_url = request.POST.get('post_url')

        if reply_comment_form.is_valid():
            post_id = request.POST.get('post')
            parent = request.POST.get('parent')
            new_reply_comment = reply_comment_form.save(commit=False)

            new_reply_comment.post = Post(pk=post_id)
            new_reply_comment.parent = Comment(id=parent)
            new_reply_comment.save()

            return redirect(f'{post_url}#{new_reply_comment.id}')
        else:
            print(reply_comment_form.errors.as_data())
            return redirect(post_url)

    return redirect('/')


def blog_like_post_view(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user

        if not post.like.filter(id=user.id).exists():
            post.like.add(user)
            post.save()
        else:
            post.like.remove(user)
            post.save()

        context = {'post': post}
        return render(request, 'blog/blog_like_post.html', context=context)

    return redirect('blog:list')


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
