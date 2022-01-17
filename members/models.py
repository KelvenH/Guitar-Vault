from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from subscriptions.models import Subscription
from django_countries.fields import CountryField


class MemberProfile(models.Model):
    """
    Member profile page holding personal information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        MemberProfile.objects.create(user=instance)
    #Existing users: just save the profile
    instance.memberprofile.save()


class MembersPlans(models.Model):
    """
    Logs history of members subscription plans current and past
    """
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