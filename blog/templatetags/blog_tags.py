from django import template
from django.db.models import Count
from django.utils import timezone

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
