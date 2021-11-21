from django.contrib import admin
from .models import Subscription


class SubsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price'
    )

    ordering = ('-price',)

admin.site.register(Subscription, SubsAdmin)
