from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='home_page'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),

    path('search/', search_view, name='search')
]
