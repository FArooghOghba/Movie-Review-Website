from django.contrib import admin

from blog.models import *


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'published_date'
    ]

    autocomplete_fields = ['categories']

    prepopulated_fields = {
        'slug': ['title']
    }

    search_fields = [
        'title',
        'content',
        'created_date'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'post',
        'created_date',
        'approved'
    ]

    # list_filter = [
    #     'author',
    #     'approved',
    #     'created_date'
    # ]
    #
    # search_fields = [
    #     'author',
    #     'content'
    # ]
