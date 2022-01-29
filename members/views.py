from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import MemberProfile
from .forms import MemberProfileForm
from site_admin.models import Accounts, Guitar_Loans
from checkout.models import Order
from guitars.models import Guitar


@login_required
def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(MemberProfile, user=request.user)
    orders = profile.orders.all()
    accounts = Accounts.objects.all()
    guitars = Guitar.objects.all()
    loans = Guitar_Loans.objects.all()
    
    if request.method == 'POST':
        form = MemberProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
        else:
            messages.error(request, 'Update failed - please ensure all fields completed correctly')
    else:
        form = MemberProfileForm(instance=profile)   
    
    template = 'members/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'accounts': accounts,
        'guitars': guitars,
        'loans': loans,
    }

    return render(request, template, context)


@login_required
def favourite_add(request, id):
    """
    function to add / remove favourite to user
    """
    guitar = get_object_or_404(Guitar, id=id)
    if guitar.favourites.filter(id=request.user.id).exists():
        guitar.favourites.remove(request.user)
    else:
        guitar.favourites.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def request_guitar(request, id):
    """
    function to request guitar loan
    1 - identify guitar tier
    2 - identify if user has plectrums to exchange matching or of a higher tier than guitar
    3 - if passes, create new guitar loan request
    4 - add guitar to users guitar rack
    5 - change guitar status to prevent other user selecting
    6 - deduct token from balance (out of scope as admin task)
    """
    if request.method == 'POST':
        
        # identify selected guitar (single object)
        guitar = Guitar.objects.get(pk=id)

        # get tier of guitar
        guitar_tier = guitar.tier

        # identify if user has active subscription and plectrum available (note sum needed in case user has multiple subscriptions at same tier)
        thisuser=request.user
        
        plat_accept = False
        gold_accept = False
        silver_accept = False
        bronze_accept = False

        # check for platinum 
        user_plat_tokens = Accounts.objects.filter(order__subscription_plan__name='Platinum',active=True,order__member_profile__user__username=thisuser).aggregate(tokens=Sum('plectrum_balance'))['tokens']
        
        if user_plat_tokens is not None or (user_plat_tokens == 0):
            plat_accept = True
        
        # check for gold
        user_gold_tokens = Accounts.objects.filter(order__subscription_plan__name='Gold',active=True,order__member_profile__user__username=thisuser).aggregate(tokens=Sum('plectrum_balance'))['tokens']
        
        if user_gold_tokens is not None or (user_gold_tokens == 0):
            gold_accept = True

        # check for silver
        user_silver_tokens = Accounts.objects.filter(order__subscription_plan__name='Silver',active=True,order__member_profile__user__username=thisuser).aggregate(tokens=Sum('plectrum_balance'))['tokens']
        
        if user_silver_tokens is not None or (user_silver_tokens == 0):
            silver_accept = True

        # check for bronze
        user_bronze_tokens = Accounts.objects.filter(order__subscription_plan__name='Bronze',active=True,order__member_profile__user__username=thisuser).aggregate(tokens=Sum('plectrum_balance'))['tokens']
        
        if user_bronze_tokens is not None or (user_bronze_tokens == 0):
            bronze_accept = True

        print("plat result", plat_accept)
        print("gold result", gold_accept)
        print("silver result", silver_accept)
        print("bronze result", bronze_accept)

        # authorise if user has pass for tier matching or higher tier than guitar
        authorise_loan = False

        if guitar_tier == 'Platinum':
            if plat_accept:
                authorise_loan = True
        
        elif guitar_tier == 'Gold':
            if plat_accept or gold_accept:
                authorise_loan = True
        
        elif guitar_tier == 'Silver':
            if plat_accept or gold_accept or silver_accept:
                authorise_loan = True

        elif guitar_tier == 'Bronze':
            if plat_accept or gold_accept or silver_accept or bronze_accept:
                authorise_loan = True

        print("authorise_loan", authorise_loan)

        if authorise_loan == True:

            instance = Guitar_Loans(guitar=guitar, user=thisuser)
            messages.success(request, 'Your guitar has successfully been added to the rack!')
            instance.save()
            # Update guiar's status to prevent other user selecting
            guitar.status="In Use"
            guitar.save()

        else:
            messages.error(request, 'Sorry, you do not have a subscription plan for that tier or any plectrums to exchange this month')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
