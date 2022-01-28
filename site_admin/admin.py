from django.contrib import admin
from .models import Accounts


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'active',
        'canx_requested',
        'canx_date',
        'plectrum_balance',
    )

    ordering = ('-active',)

admin.site.register(Accounts, AccountsAdmin)
