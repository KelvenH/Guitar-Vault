from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Subscription

def all_subscriptions(request):

    subscriptions = Subscription.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/subscriptions.html', context)
