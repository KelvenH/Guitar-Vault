from django.contrib import admin
from .models import Accounts
from .models import Guitar_Loans

class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'active',
        'canx_requested',
        'canx_date',
        'plectrum_balance',
    )

    ordering = ('-active',)


class GuitarLoansAdmin(admin.ModelAdmin):
    list_display = (
        'guitar',
        'user',
        'loan_status',
        'requested_date',
        'shipped_date',
        'returned_date',
    )

    ordering = ('requested_date', 'loan_status')


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Guitar_Loans, GuitarLoansAdmin)