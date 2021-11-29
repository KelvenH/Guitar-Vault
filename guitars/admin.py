from django.contrib import admin
from .models import Guitar, Category


class GuitarAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'guitar_model',
        'category',
        'tier',
        'status',
        'condition',
        'rating_condition',
        'rating_overall',
    )

    ordering = ('brand', 'guitar_model')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Guitar, GuitarAdmin)
admin.site.register(Category, CategoryAdmin)
