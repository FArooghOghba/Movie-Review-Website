from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list_view, name='list'),
    path('single/<slug:post_slug>', blog_single_view, name='single'),

    path('search/', blog_search_view, name='search')
]
