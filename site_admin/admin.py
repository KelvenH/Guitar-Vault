from django.contrib import admin
from .models import Accounts


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'order',
        'active',
        'canx_date',
        'plec_plat',
        'plec_gold',
        'plec_slvr',
        'plec_brnz',
    )

    ordering = ('active', 'user')

admin.site.register(Accounts, AccountsAdmin)
