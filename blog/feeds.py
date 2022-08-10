from django.contrib.syndication.views import Feed
from django.utils import timezone

from blog.models import Post


class LatestPostsFeed(Feed):
    title = "Movie pro site news"
    link = "rss/feed/"
    description = "Updates on changes and additions to movies."

    def items(self):
        return Post.objects.filter(
            published_date__lte=timezone.now(),
            status=True
        )

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
