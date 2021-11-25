from django.shortcuts import render
from guitars.models import Guitar

# Create your views here.
def index(request):
    """ View to return the index page """
    
    guitars = Guitar.objects.all()

    context = {
        'guitars': guitars,
    }

    return render(request, 'home/index.html', context)
