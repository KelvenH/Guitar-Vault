from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Subscription

def all_subs(request):

    sub = Subsciption.objects.all()

return render(request, 'subscriptions/subscriptions.html')
