from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'rating',
        'release_date',
        'runtime'
    ]

    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
