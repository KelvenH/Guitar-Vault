from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib import messages
from guitars.models import Guitar
from checkout.models import Order
from .models import Accounts
from .forms import GuitarForm
from .forms import OrderForm


@login_required
def site_admin(request):
    """ View to display the admin page """

    # Redirect non-super users to home page
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    return render(request, 'site_admin/site_admin.html')


class GuitarList(LoginRequiredMixin, ListView):
    """ Uses a class view to display all guitar in the database """
    
    template_name = 'site_admin/list_guitars.html'
    model = Guitar


@login_required
def edit_guitar(request, guitar_id):
    """ Edit guitar in the database """
    # Redirect non-super users to home page
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    guitar = get_object_or_404(Guitar, pk=guitar_id)

    if request.method == 'POST':
        form = GuitarForm(request.POST, request.FILES, instance=guitar)

        if form.is_valid():
            form.save()
            messages.success(request, 'Guitar details successfully updated!')
            return redirect(reverse('guitar_detail', args=[guitar.id]))

        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')

    else:
        form = GuitarForm(instance=guitar)

    template = 'site_admin/edit_guitar.html'
    context = {
        'form': form,
        'guitar': guitar,
    }

    return render(request, template, context)


@login_required
def delete_guitar(request, guitar_id):
    """ Delete guitar from the database """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    guitar = get_object_or_404(Guitar, pk=guitar_id)
    guitar.delete()
    messages.success(request, 'Guitar has been deleted from the vault!')
    return redirect(reverse('guitarlist'))


@login_required
def add_guitar(request):
    """ Add new guitar to the database """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GuitarForm(request.POST, request.FILES)
        if form.is_valid():
            guitar = form.save()
            messages.success(request, 'Another guitar successfully added to the vault!')
            return redirect(reverse('guitar_detail', args=[guitar.id]))
        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')
    else:
        form = GuitarForm()

    template = 'site_admin/add_guitar.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


class OrderList(LoginRequiredMixin, ListView):
    """ Uses a class view to display all orders in the database """

    template_name = 'site_admin/list_orders.html'
    model = Order


@login_required
def edit_order(request, order_id):
    """ Edit order in the database """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)

        if form.is_valid():
            form.save()
            messages.success(request, 'Order details successfully updated!')
            return redirect(reverse('orderlist'))

        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')

    else:
        form = OrderForm(instance=order)

    template = 'site_admin/edit_order.html'
    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)


@login_required
def delete_order(request, order_id):
    """ Delete order from the database """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    messages.success(request, 'Order has been deleted from the vault!')
    return redirect(reverse('orderlist'))


@login_required
def add_order(request):
    """ Add new order to the database """
    
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            messages.success(request, 'Order successfully added!')
            return redirect(reverse('orderlist'))
        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')
    else:
        form = OrderForm()

    template = 'site_admin/add_order.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def AllAccounts(request):
    """
    Display Accounts
    """
    accounts = Accounts.objects.all()
        
       
    template = 'site_admin/accounts.html'
    context = {
        'accounts': accounts,

    }

    return render(request, template, context)


@login_required
def canx_account(request, id):
    """
    Function to ammend account status to cancelled
    """
    account = get_object_or_404(Accounts, id=id)
    account.active = False
    account.canx_date = datetime.now()
    account.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def award_plectrums(request):
    """
    Update Plectrum Balances; for project purposes, this function will reward 1 plectrum (internal exchange token), in 'real-world' this would need to incorporate a diarised mechanism to only operate on a monthly cycle.
    """
    accounts = Accounts.objects.all()
        
    for account in accounts:
        plan = account.order.subscription_plan
        active = account.active

        if bool(active) == True:        
            account.plectrum_balance += 1
            account.save()

        else:
            messages.error(request, 'There was an error.  \
                Please check plectrums updated correctly')
     
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


