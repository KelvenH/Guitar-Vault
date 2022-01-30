from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class MemberProfile(models.Model):
    """
    Member profile page holding personal information with 1to1
    relationship with user model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=False, blank=False)
    default_street_address1 = models.CharField(max_length=80, null=False,
                                               blank=False)
    default_street_address2 = models.CharField(max_length=80, blank=True,
                                               default="")
    default_town_or_city = models.CharField(max_length=40, null=False,
                                            blank=False)
    default_county = models.CharField(max_length=80, blank=True, default="")
    default_postcode = models.CharField(max_length=20, blank=True, default="")
    default_country = CountryField(blank_label='Country', null=False,
                                   blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile following a save to the User model
    """
    if created:
        # Create a new profile instance for new user registrations
        MemberProfile.objects.create(user=instance)
    # Update existing profile for existing users
    instance.memberprofile.save()
