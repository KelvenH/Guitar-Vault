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

    if request.method == 'POST':
        bag = request.session.get('bag',{})
        form_data = {
            'subscription_plan': request.POST['subscription_plan'],
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order_form.save()
            for item_id, item_data in bag.items():
                try:
                    subscription = Subscription.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        


    else:
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

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.\
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
