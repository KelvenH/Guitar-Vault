from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import Subscription


def bag_contents(request):

    bag_items = []
    bag_total = 0
    bag = request.session.get('bag', {})

    for subscription_id, quantity in bag.items():
        subscription = get_object_or_404(Subscription, pk=subscription_id)
        bag_total = subscription.price
        bag_items.append({
            'subscription_id': subscription_id,
            'subscription': subscription
        })

    context = {
        'bag_items': bag_items,
        'bag_total': bag_total,
    }

    return context
