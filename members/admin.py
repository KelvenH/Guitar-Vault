from django.contrib import admin
from .models import MembersPlans


class MembersPlansAdmin(admin.ModelAdmin):
    list_display = (
        'member_profile',
        'subscription_plan',
        'subscription_price',
        'start_date',
        'active',
        'canx_date',
    )

    ordering = ('member_profile', 'active')


admin.site.register(MembersPlans, MembersPlansAdmin)
