from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    """
    View to see checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in our bag, take a look at our subscription plans to proceed")
        return redirect(reverse('subscriptions'))

    # get total cost from bag
    current_bag = bag_contents(request)
    total = current_bag['bag_total']
    # convert total to integer for Stripe
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K09ihIfuGDQGaewEbM0Wd0V3LX4bM3mtQrEisAhQFHvjrBMsL6zkk4EEg49kOermXCi7ZSHQ8wvv0AG8uX0HUHI00J6V68xZs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
