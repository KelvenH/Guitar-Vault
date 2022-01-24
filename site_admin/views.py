from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GuitarForm


""" View to display the admin page """
@login_required
def site_admin(request):

    # Redirect non-super users to home page
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    
    context = {
        
    }

    return render(request, 'site_admin/site_admin.html', context)


""" Add new guitar to the database """
def add_guitar(request):
    if request.method == 'POST':
        form = GuitarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Another guitar successfully added to the vault!')
            return redirect(reverse('add_guitar'))
        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')
    else:        
        form = GuitarForm()

    template = 'site_admin/add_guitar.html'
    context = {
        'form': form,
    }

    return render(request, template, context)