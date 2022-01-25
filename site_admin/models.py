from django.db import models

"""
class Accounts(models.Model):
    
    Logs history of members subscription plans current and past
    
    # match user to member profile
    member_profile = models.ForeignKey(MemberProfile,
                                       on_delete=models.SET_NULL,
                                       null=True, blank=True)

    # get list of subscription plans purchased
    subscription_plan = models.ForeignKey(Subscription, null=False,
                                          blank=False,
                                          on_delete=models.PROTECT)
    # capture price paid
    subscription_price = models.DecimalField(max_digits=4, decimal_places=2,
                                             null=False, default=0)

    # date plan purchased
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    # is plan active or cancelled
    active = models.BooleanField(default=False)

    # date if plan cancelled 
    canx_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    """