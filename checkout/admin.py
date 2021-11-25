from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'subscription_price',)

    fields = ('order_number', 'date', 'subscription_plan',
              'subscription_price', 'full_name', 'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city',
              'postcode', 'county', 'country',)

    list_display = ('order_number', 'date', 'full_name', 'subscription_plan',
                    'subscription_price',)

    ordering = ('full_name',)


admin.site.register(Order, OrderAdmin)
