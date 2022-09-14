from django import template
from django.db.models import Count
from django.utils import timezone

import hashlib
from urllib.parse import urlencode
from django.utils.safestring import mark_safe

from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/blog_post_category_count.html')
def blog_categories_count():
    all_post_count = Post.objects.count()

    categories_count = Category.objects \
        .annotate(cat_count=Count('post')) \
        .order_by('-cat_count')

    return {
        'categories_count': categories_count,
        'all_post_count': all_post_count
    }


@register.inclusion_tag('blog/blog_recent_news.html')
def blog_recent_news():
    recent_news = Post.objects.all()[:3]

    return {'recent_news': recent_news}


@register.inclusion_tag('blog/blog_archives.html')
def archives():
    this_year = timezone.now().year
    counted_month_posts = Post.objects \
        .filter(published_date__year=this_year) \
        .dates('published_date', 'month') \
        .annotate(count=Count('id')) \
        .values('datefield', 'count') \
        .order_by('-datefield')

    return {'counted_month_posts': counted_month_posts}


# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    default = "identicon"
    return f"https://www.gravatar.com/avatar/" \
           f"{hashlib.md5(email.lower().encode('utf-8')).hexdigest()}?{urlencode({'d':default, 's': str(size)})}"


# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe(f'{url}{size}{size}')
