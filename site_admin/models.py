from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order

class Accounts(models.Model):

    """
    Members accounts used to track active subscriptions and award plectrums
    """
    class Meta:
        verbose_name_plural = 'Accounts'

    # match user to member profile
    user = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='accounts_user')

    # get subscription plans purchased
    subscription_type = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='accounts_sub_type')

    # date plan purchased
    start_date = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False,related_name='accounts_start_date')

    # Status (active or cancelled)
    active = models.BooleanField(default='TRUE')

    # date if plan cancelled 
    canx_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    # Plectrums (loan exchange token)
    Plec_Plat = models.IntegerField(null=True, blank=True, default=0)
    Plec_Gold = models.IntegerField(null=True, blank=True, default=0)
    Plec_Slvr = models.IntegerField(null=True, blank=True, default=0)
    Plec_Brnz = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.user.username
