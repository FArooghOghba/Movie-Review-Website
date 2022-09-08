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


class CastCrew(models.Model):

    CAREER_CHOICES = [
        ('Actor', 'Actor'),
        ('Actress', 'Actress'),
        ('Director', 'Director'),
        ('Writer', 'Writer'),
        ('Producer', 'Producer'),
        ('Music', 'Music'),
    ]

    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to='cast_crew_image/',
        default='cast_crew_image/blank-profile-picture.png'
    )
    career = models.CharField(max_length=10, choices=CAREER_CHOICES, default="Actor")
    cast = models.BooleanField(default=False)
    crew = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=False, unique=True)
    genre = models.ManyToManyField(Genre)
    cast_crew = models.ManyToManyField(
        CastCrew,
        related_name='cast_crew',
        through='role'
    )
    synopsis = models.TextField()
    rating = GenericRelation(Rating, related_query_name='movie')
    poster = models.ImageField(upload_to='movie_poster/')
    trailer = models.URLField()
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


class Role(models.Model):
    role_name = models.CharField(max_length=64)
    cast_crew = models.ForeignKey(
        CastCrew,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.role_name
