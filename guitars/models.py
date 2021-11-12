from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    """
    String method
    """
    def __str__(self):
        return self.name

    
    """
    Model method
    """
    def get_friendly_name(self):
        return self.get_friendly_name


class Guitar(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=25)
    guitar_model = models.CharField(max_length=25)
    tier = models.CharField(max_length=25, null=True, blank=True)
    status = models.CharField(max_length=25, null=True, blank=True)
    owner = models.CharField(max_length=25, null=True, blank=True)
    handed = models.CharField(max_length=25, null=True, blank=True)
    no_strings = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    approx_age_years = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    condition = models.CharField(max_length=25, null=True, blank=True)
    construction = models.CharField(max_length=25, null=True, blank=True)
    body_wood = models.CharField(max_length=25, null=True, blank=True)
    body_top = models.CharField(max_length=25, null=True, blank=True)
    tuners = models.CharField(max_length=25, null=True, blank=True)
    frets = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    scale_length = models.CharField(max_length=25, null=True, blank=True)
    neck_wood = models.CharField(max_length=25, null=True, blank=True)
    neck_profile = models.CharField(max_length=25, null=True, blank=True)
    no_pickups = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    pickups_desc = models.TextField()
    controls = models.CharField(max_length=25, null=True, blank=True)
    owners_additional_comments = models.TextField()
    rating_condition = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    rating_overall = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    image_id = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
