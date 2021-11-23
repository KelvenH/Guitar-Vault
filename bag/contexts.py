from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    
    total_VAT = total * Decimal(settings.VAT_PERCENTAGE/100)

    context = {
        'bag_items': bag_items,
        'total': total,
        'total_VAT': total_VAT,
    }

    return context
