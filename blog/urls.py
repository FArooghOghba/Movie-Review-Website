from django.urls import path
from blog.views import *

from blog.feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', blog_list_view, name='list'),
    path('single/<slug:post_slug>/', blog_single_view, name='single'),

    path('like/<int:post_id>/', blog_like_post_view, name='like_post'),
    path('search/', blog_search_view, name='search'),
    path('category/<slug:cat_slug>/', blog_list_view, name='category'),
    path('tag/<slug:tag_slug>/', blog_list_view, name='tag'),
    path('comment/reply/', blog_reply_comment_view, name='reply_comment'),
    path('rss/feed/', LatestPostsFeed()),
]
