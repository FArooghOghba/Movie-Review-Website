from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from movie.models import Movie


class MovieSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Movie.objects.all()

    def lastmod(self, obj):
        return obj.release_date

    def location(self, item):
        return reverse('movie:single', kwargs={'movie_slug': item.slug})
