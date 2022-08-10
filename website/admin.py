from django.contrib import admin
from .models import Contact, Newsletter


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'created_date'
    ]

    list_filter = ['email']
    search_fields = ['name', 'subject']
    empty_value_display = '-empty-'


admin.site.register(Newsletter)
