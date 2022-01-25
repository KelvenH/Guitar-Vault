from django.contrib import admin
from .models import Accounts


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subscription_type',
        'start_date',
        'active',
        'canx_date',
        'Plec_Plat',
        'Plec_Gold',
        'Plec_Slvr',
        'Plec_Brnz',
    )

    ordering = ('active', 'user')

admin.site.register(Accounts, AccountsAdmin)
