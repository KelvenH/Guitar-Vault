from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    # String method
    def __str__(self):
        return self.name

    # Model method
    def get_friendly_name(self):
        return self.get_friendly_name


class Guitar(models.Model):
    # Category (with choices to create dropdown selection for users)
    # PROTECT prevents deletion of the primary key (categories)
    category = models.ForeignKey(Category, null=False, blank=False,
                                 on_delete=models.PROTECT)

    # Brand & Model
    brand = models.CharField(max_length=25)
    guitar_model = models.CharField(max_length=50)

    # Tier
    PLATINUM = 'Platinum'
    GOLD = 'Gold'
    SILVER = 'Silver'
    BRONZE = 'Bronze'

    TIER_CHOICES = [
        (PLATINUM, 'Platinum'),
        (GOLD, 'Gold'),
        (SILVER, 'Silver'),
        (BRONZE, 'Bronze'),
    ]
    tier = models.CharField(max_length=10, choices=TIER_CHOICES,
                            default=BRONZE)

    # Status
    status = models.CharField(max_length=25, null=True, blank=True)

    # Right / Left Handed
    RIGHT = 'Right'
    LEFT = 'Left'

    HANDED_CHOICES = [
        (RIGHT, 'Right'),
        (LEFT, 'Left'),
    ]
    handed = models.CharField(max_length=5, choices=HANDED_CHOICES,
                              default=RIGHT)

    # No. Strings and Age
    no_strings = models.DecimalField(max_digits=2, decimal_places=0, null=True,
                                     blank=True)
    approx_age_years = models.DecimalField(max_digits=2, decimal_places=0,
                                           null=True, blank=True)

    # Condition
    EXCELLENT = 'Excellent'
    GOOD = 'Good'
    COSMETIC = 'Cosmetic'
    DEFECTIVE = 'Defective'
    CONDITION_CHOICES = [
        (EXCELLENT, 'Excellent'),
        (GOOD, 'Good'),
        (COSMETIC, 'Well Used (displays cosmetic signs of use only)'),
        (DEFECTIVE, 'Some form of damage / wear which affects performance.'),
        ]
    condition = models.CharField(max_length=250, choices=CONDITION_CHOICES,
                                 default=GOOD)
    construction = models.CharField(max_length=25, null=True, blank=True)
    body_wood = models.CharField(max_length=50, null=True, blank=True)
    body_top = models.CharField(max_length=50, null=True, blank=True)
    tuners = models.CharField(max_length=50, null=True, blank=True)

    # No. Frets
    FRETS_20 = 20
    FRETS_22 = 22
    FRETS_24 = 24
    FRETS_CHOICES = [
        (FRETS_20, 20),
        (FRETS_22, 22),
        (FRETS_24, 24),
        ]
    frets = models.DecimalField(max_digits=2, decimal_places=0,
                                choices=FRETS_CHOICES, default=FRETS_22)

    # Additional Info
    scale_length = models.CharField(max_length=25, null=True, blank=True)
    neck_wood = models.CharField(max_length=25, null=True, blank=True)
    neck_profile = models.CharField(max_length=25, null=True, blank=True)
    no_pickups = models.DecimalField(max_digits=1, decimal_places=0,
                                     null=True, blank=True)
    pickups_desc = models.TextField()
    controls = models.CharField(max_length=250, null=True, blank=True)
    owners_additional_comments = models.TextField()
    rating_condition = models.DecimalField(max_digits=2, decimal_places=0,
                                           null=True, blank=True)
    rating_overall = models.DecimalField(max_digits=2, decimal_places=0,
                                         null=True, blank=True)
    image_id = models.ImageField(null=True, blank=True)

    # Used to identify images to appear in 'Featured' carousel
    featured = models.BooleanField(default=False)

    # Used to capture user's favourited guitars
    favourites = models.ManyToManyField(User, related_name='favourite',
                                        default=None, blank=True)

    def __str__(self):
        return self.guitar_model
