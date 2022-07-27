import star_ratings.models
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from . import models


# Register your models here.
# class RatingAverage(GenericInlineModelAdmin):
#     model = star_ratings.models.Rating


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'release_date',
        'runtime'
    ]
    search_fields = ['title__istartswith', 'release_date']

    prepopulated_fields = {
        'slug': ['title']
    }

    # inlines = [RatingAverage]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
