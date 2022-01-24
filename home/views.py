from django.shortcuts import render
from guitars.models import Guitar


# Create your views here.
def index(request):
    """ View to return the index page """
    
    guitars = Guitar.objects.all()
    # Identify guitars with 'Featured' flag for inclusion in image carousel
    display_id = []
    display_image = []

    for guitar in guitars:
        if guitar.image_id:
            id = guitar.id
            image_url = guitar.image_id.url
            featured = guitar.featured
            if featured:
                display_id.append(id)
                display_image.append(image_url)


    context = {
        'guitars': guitars,
        'display_id': display_id,
        'display_image': display_image,
    }

    return render(request, 'home/index.html', context)
    