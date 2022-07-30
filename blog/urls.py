from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list_view, name='list'),
    path('single/', blog_single_view, name='single'),
]
