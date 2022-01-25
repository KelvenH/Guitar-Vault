from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from guitars.models import Guitar
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
            guitar = form.save()
            messages.success(request, 'Another guitar successfully added to the vault!')
            return redirect(reverse('guitar_detail', args=[guitar.id]))
        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')
    else:        
        form = GuitarForm()

    template = 'site_admin/add_guitar.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


""" Uses a class view to display all guitar in the database """
class GuitarList(ListView):
    template_name = 'site_admin/list_guitars.html'
    model = Guitar


""" Edit guitar in the database """
def edit_guitar(request, guitar_id):
    guitar = get_object_or_404(Guitar, pk=guitar_id)
    
    if request.method == 'POST':
        form = GuitarForm(request.POST, request.FILES, instance=guitar)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Guitar details successfully updated!')
            return redirect(reverse('guitar_detail', args=[guitar.id]))

        else:
            messages.error(request, 'Oops, computer says NO - check the form for errors')
    
    else:        
        form = GuitarForm(instance=guitar)
    
    template = 'site_admin/edit_guitar.html'
    context = {
        'form': form,
        'guitar': guitar,
    }

    return render(request, template, context)


""" Delete guitar from the database """
def delete_guitar(request, guitar_id):
    guitar = get_object_or_404(Guitar, pk=guitar_id)
    guitar.delete()
    messages.success(request, 'Guitar has been deleted from the vault!')
    return redirect(reverse('guitarlist'))
