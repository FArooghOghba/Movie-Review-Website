from django import template
from django.utils import timezone

from blog.models import *


register = template.Library()


@register.inclusion_tag('website/latest_news.html')
def website_latest_news():
    latest_news = Post.objects.filter(
        published_date__lte=timezone.now(),
        status=True
    )[:3]

    return {'latest_news': latest_news}
