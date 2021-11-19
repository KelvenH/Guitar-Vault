from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Guitar

def all_guitars(request):
    """ A view to show all guitars, including sorting and search queries """

    guitars = Guitar.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Provide a guitar brand or model name for me to search for")
                return redirect(reverse('guitars'))
            
            queries = Q(brand__icontains=query) | Q(guitar_model__icontains=query)
            guitars = guitars.filter(queries)

    context = {
        'guitars': guitars,
        'search_term': query,
    }

    return render(request, 'guitars/guitars.html', context)


def guitar_detail(request, guitar_id):
    """ A view to show guitar details """

    guitar = get_object_or_404(Guitar, pk=guitar_id)

    context = {
        'guitar': guitar,
    }

    return render(request, 'guitars/guitar_detail.html', context)