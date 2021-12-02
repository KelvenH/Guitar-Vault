from django.shortcuts import render, redirect


def view_bag(request):
    """ View to render the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, subscription_id):
    """Add subscription plan to bag"""

    quantity = 1
    redirect_url = request.POST.get('redirect_url')

    # Get existing bag in session or create new
    bag = request.session.get('bag', {})

    # Prevent different plans in bag by removing existing id before adding new

    if bag:

        bag.popitem()
        bag[subscription_id] = quantity

    else:
        bag[subscription_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
