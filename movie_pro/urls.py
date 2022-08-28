"""movie_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from movie.sitemaps import MovieSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'movie': MovieSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('movie/', include('movie.urls')),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('captcha/', include('captcha.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
]

# With this urlpatterns, Django's development server is capable of serving media files.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
