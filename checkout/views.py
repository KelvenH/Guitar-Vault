from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order
from subscriptions.models import Subscription
from bag.contexts import bag_contents

import stripe

def checkout(request):
    """
    View to see checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # get the chosen subscription from the bag
        bag = request.session.get('bag', {})
        # also get the form input values
        form_data = {
            'subscription_plan': request.POST['subscription_plan'],
            'subscription_price': request.POST['subscription_price'],
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
            order = order_form.save()
                        
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form \
                Please check your information')
            print(order_form.errors)
                
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


def checkout_success(request, order_number):
    """
    View to confirm successful checkout
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order has been successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
