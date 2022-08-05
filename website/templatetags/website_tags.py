from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('website/latest_news.html')
def website_latest_news():
    latest_news = Post.objects.all()[:3]

    return {'latest_news': latest_news}
