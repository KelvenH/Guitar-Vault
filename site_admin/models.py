from django.db import models
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from checkout.models import Order


class Accounts(models.Model):

    """
    Members accounts used to track active subscriptions and award plectrums
    """
    class Meta:
        verbose_name_plural = 'Accounts'

    # match order for account
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='accounts')

    # Status (active or cancelled)
    active = models.BooleanField(default=True)

    # Canx Requested by user
    canx_requested = models.BooleanField(default=False)

    # date if plan cancelled
    canx_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    # Plectrums (loan exchange token)
    plectrum_balance = models.IntegerField(null=True, blank=True, default=1)


    def __str__(self):
        return self.order

# Reciver listens for new orders and creates new account
@receiver(post_save, sender=Order)
def create_account(sender, instance, created, **kwargs):

    if created:
        Accounts.objects.create(order=instance)
