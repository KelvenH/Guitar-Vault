from django.shortcuts import render
from .models import Guitar

def all_guitars(request):
    """ A view to show all guitars, including sorting and search queries """

    guitars = Guitar.objects.all()

    context = {
        'guitars': guitars,
    }

    return render(request, 'guitars/guitars.html', context)
