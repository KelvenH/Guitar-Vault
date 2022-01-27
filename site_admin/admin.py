from django.contrib import admin
from .models import Accounts


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'order',
        'active',
        'canx_date',
        'plectrum_balance',
    )

    ordering = ('-active', '-user',)

admin.site.register(Accounts, AccountsAdmin)
