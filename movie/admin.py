from django.contrib import admin
import star_ratings.models
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from . import models


# Register your models here.
# class RatingAverage(GenericInlineModelAdmin):
#     model = star_ratings.models.Rating


class RoleInline(admin.TabularInline):
    model = models.Role
    extra = 1
    autocomplete_fields = ['cast_crew']


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'release_date',
        'runtime'
    ]
    search_fields = ['title__istartswith', 'release_date']
    # autocomplete_fields = ['cast_crew']

    prepopulated_fields = {
        'slug': ['title']
    }

    inlines = [RoleInline]


@admin.register(models.CastCrew)
class CastCrewAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # autocomplete_fields = ['role']
    list_display = [
        'name',
        'career',
        'added_date'
    ]
    inlines = [RoleInline]


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    search_fields = ['role_name']
    list_display = [
        'role_name'
    ]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
