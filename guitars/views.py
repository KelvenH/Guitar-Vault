from django.shortcuts import render, get_object_or_404
from .models import Guitar

def all_guitars(request):
    """ A view to show all guitars, including sorting and search queries """

    guitars = Guitar.objects.all()

    context = {
        'guitars': guitars,
    }

    return render(request, 'guitars/guitars.html', context)


def guitar_detail(request, guitar_id):
    """ A view to show guitar details """

    guitar = get_object_or_404(Guitar, pk=guitar_id)

    context = {
        'guitar': guitar,
    }

    return render(request, 'guitars/guitar_detail.html', context)