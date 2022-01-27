from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib.auth.models import User
from checkout.models import Order


class Accounts(models.Model):

    """
    Members accounts used to track active subscriptions and award plectrums
    """
    class Meta:
        verbose_name_plural = 'Accounts'

    # match account to a user
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # creates error in admin console "Accounts with this User already exists."
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # django error "UNIQUE constraint failed"

    #user = models.ManyToManyField(User)
    # creates error in terminal "..must not be ManyToManyField"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    
    # Status (active or cancelled)
    active = models.BooleanField(default=True)

    # date if plan cancelled 
    canx_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    # Plectrums (loan exchange token)
    plectrum_balance = models.IntegerField(null=True, blank=True, default=1)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Order)
def create_account(sender, instance, created, **kwargs):
    
    print("sender =", sender)
    print("instance1 =", instance)
    if created:
        
        order = instance.order_number
        print("instance2 =", instance)
        Accounts.objects.create(order=instance, defaults={
            "user": order.member_profile,
            "order": order.order_number,
            }
        )

    instance.account.save()