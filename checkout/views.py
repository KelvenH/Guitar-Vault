from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe
from subscriptions.models import Subscription
from members.forms import MemberProfileForm
from members.models import MemberProfile
from bag.contexts import bag_contents
from .models import Order
from .forms import OrderForm


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

            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form \
                Please check your information')
            print(order_form.errors)

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in our bag, take a look \
                                    at our subscription plans to proceed")
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

        # Pre-fill form with user info from profile
        if request.user.is_authenticated:
            try:
                profile = MemberProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except:
                order_form = OrderForm()
        else:
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

    if request.user.is_authenticated:
        profile = MemberProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_town_or_city': order.town_or_city,
            'default_county': order.county,
            'default_postcode': order.postcode,
            'default_country': order.country,
        }
        user_profile_form = MemberProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
