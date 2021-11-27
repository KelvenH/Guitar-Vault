from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('subscription_plan', 'full_name', 'email',
                  'phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode',
                  'county', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Rename fields to user friendly display on form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'subscription_plan': 'Subscription Plan',
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone No.',
            'street_address1': 'Address 1',
            'street_address2': 'Address 2',
            'town_or_city': 'Town / City',
            'county': 'County',
            'postcode': 'Post Code',
            'country': 'Country',
        }

        # On page load, cursor placed in full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Add asterisk to any fields set as required /mandatory
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set fields to user friendly names defined above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Applies class to all inout fields for consistant styles across form (inc. Stripe fields)
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove default fields labels as placeholders will be used
            self.fields[field].label = False
