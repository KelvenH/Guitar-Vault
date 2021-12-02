from django.db import models


class Subscription(models.Model):

    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    delivery = models.CharField(max_length=25, default=False)
    re_stringed = models.BooleanField(default=False)
    set_up = models.BooleanField(default=False)

    # String method
    def __str__(self):
        return self.name
