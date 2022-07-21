from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='home_page'),
    path('movie/', movie_list_view, name='movie_list'),
    path('blog/', blog_list_view, name='blog_list'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]
