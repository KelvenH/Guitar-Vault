from django.shortcuts import render, get_object_or_404
from .models import MemberProfile

def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(MemberProfile, user=request.user)
    template = 'members/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
