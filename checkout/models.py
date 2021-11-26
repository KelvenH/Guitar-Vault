import uuid

from django.db import models
from django.conf import settings

from subscriptions.models import Subscription


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    subscription_plan = models.ForeignKey(Subscription, null=False,
                                          blank=False,
                                          on_delete=models.PROTECT)
    subscription_price = models.DecimalField(max_digits=4, decimal_places=2,
                                             null=False, default=0)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    # null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    # stripe_pid = models.CharField(max_length=254, null=False,
    # blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number if
        not already set
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number