from django.contrib import admin

from blog.models import *


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'published_date'
    ]

    prepopulated_fields = {
        'slug': ['title']
    }
