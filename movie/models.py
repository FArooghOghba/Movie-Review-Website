from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

from star_ratings.models import Rating


# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=False, unique=True)
    genre = models.ManyToManyField(Genre)
    synopsis = models.TextField()
    rating = GenericRelation(Rating, related_query_name='movie')
    poster = models.ImageField(upload_to='movie_poster/')
    trailer = models.URLField()
    # cast_crew
    runtime = models.DurationField()
    release_date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date']

    def get_absolute_url(self):
        return reverse('movie:single', kwargs={'movie_slug': self.slug})

    def __str__(self):
        return self.title
