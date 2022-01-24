from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


""" View to display the admin page """
@login_required
def site_admin(request):

    # Redirect non-super users to home page
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    
    context = {
        
    }

    return render(request, 'site_admin/site_admin.html', context)