from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('subscription_plan', 'subscription_price', 'full_name', 'email',
                  'phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode',
                  'county', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Rename fields to user friendly display on form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'subscription_price': 'subscription_price',
            'subscription_plan': 'subscription_plan',
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

        """ 
        Subscription plan and price set as hidden fields, these will take
        their input values from the bag in the front end
        """
        self.fields['subscription_price'].widget = forms.HiddenInput()
        self.fields['subscription_plan'].widget = forms.HiddenInput()
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
