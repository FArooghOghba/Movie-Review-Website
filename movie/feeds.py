from django.contrib.syndication.views import Feed

from movie.models import Movie


class LatestMoviesFeed(Feed):
    title = "Movie pro site news"
    link = "rss/feed/"
    description = "Updates on changes and additions to movies."

    def items(self):
        return Movie.objects \
            .prefetch_related('genre', 'rating') \
            .order_by('-rating__average')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.synopsis
