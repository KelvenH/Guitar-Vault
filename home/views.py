from django.shortcuts import render
from guitars.models import Guitar

# Create your views here.
def index(request):
    """ View to return the index page """
    
    guitars = Guitar.objects.all()
    display = []

    for guitar in guitars:
        image_url = guitar.image_id.url
        featured = guitar.featured
        if featured:
            display.append(image_url)

    context = {
        'guitars': guitars,
        'display': display,
    }

    return render(request, 'home/index.html', context)
