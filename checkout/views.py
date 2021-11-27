from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    View to see checkout form
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in our bag, take a look at our subscription plans to proceed")
        return redirect(reverse('subscriptions'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K09ihIfuGDQGaewEbM0Wd0V3LX4bM3mtQrEisAhQFHvjrBMsL6zkk4EEg49kOermXCi7ZSHQ8wvv0AG8uX0HUHI00J6V68xZs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
