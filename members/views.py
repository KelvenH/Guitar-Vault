from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import MemberProfile
from .forms import MemberProfileForm
from checkout.models import Order
from guitars.models import Guitar


@login_required
def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(MemberProfile, user=request.user)
    orders = profile.orders.all()
    guitars = Guitar.objects.all()
    
    if request.method == 'POST':
        form = MemberProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
        else:
            messages.success(request, 'Update failed - please ensure all fields completed correctly')
    else:
        form = MemberProfileForm(instance=profile)   
    
    template = 'members/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'guitars': guitars,
    }

    return render(request, template, context)


# function to add / remove favourite to user
@login_required
def favourite_add(request, id):
    guitar = get_object_or_404(Guitar, id=id)
    if guitar.favourites.filter(id=request.user.id).exists():
        guitar.favourites.remove(request.user)
    else:
        guitar.favourites.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
