from django.shortcuts import render, get_object_or_404
from .models import MemberProfile
from .forms import MemberProfileForm

def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(MemberProfile, user=request.user)

    form = MemberProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'members/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
