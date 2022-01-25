from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from guitars.models import Guitar
from checkout.models import Order


class GuitarForm(forms.ModelForm):

    class Meta:
        model = Guitar
        fields = '__all__'
    
    """ Crispy Form Layout Helper used to custom place fields on form as opposed to single column layout. 
    Acknowledgement: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#basic-form-rendering"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False #prevents the helper adding a closing form tag which repositions the html layout placing the submit button outside of the form
        self.helper.layout = Layout(
            Row(
                Column('category', css_class='form-group col-6 col-lg-2'),
                Column('brand', css_class='form-group col-6 col-lg-2'),
                Column('guitar_model', css_class='form-group col-6 col-lg-2'),
                Column('tier', css_class='form-group col-6 col-lg-2'),
                Column('image_id', css_class='form-group col-12 col-lg-4'),
            ),
            Row(
                Column('status', css_class='form-group col-6 col-lg-2'),
                Column('handed', css_class='form-group col-6 col-lg-2'),
                Column('condition', css_class='form-group col-6 col-lg-2'),
                Column('rating_condition', css_class='form-group col-6 col-lg-2'),
                Column('rating_overall', css_class='form-group col-6 col-lg-2'),
                Column('featured', css_class='form-group col-6 col-lg-2 mb-0 d-flex align-items-end'),
            ),
            Row(
                Column('no_strings', css_class='form-group col-6 col-lg-2'),
                Column('approx_age_years', css_class='form-group col-6 col-lg-2'),
                Column('tuners', css_class='form-group col-6 col-lg-2'),
                Column('frets', css_class='form-group col-6 col-lg-2'),
                Column('no_pickups', css_class='form-group col-6 col-lg-2'),
                Column('controls', css_class='form-group col-6 col-lg-2'),
            ),
            Row(
                Column('construction', css_class='form-group col-6 col-lg-2'),
                Column('body_wood', css_class='form-group col-6 col-lg-2'),
                Column('body_top', css_class='form-group col-6 col-lg-2'),
                Column('neck_wood', css_class='form-group col-6 col-lg-2'),
                Column('neck_profile', css_class='form-group col-6 col-lg-2'),
            ),
            Row(
                Column('pickups_desc', css_class='form-group col-12 col-lg-5'),
                Column('owners_additional_comments', css_class='form-group col-12 col-lg-5'),
                Column('favourites', css_class='form-group col-12 col-lg-2'),
            ),
        )


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 
        self.helper.layout = Layout(
            Row(
                Column('order_number', css_class='form-group col-6 col-lg-2'),
                Column('member_profile', css_class='form-group col-6 col-lg-2'),
                Column('full_name', css_class='form-group col-12 col-lg-4'),
                Column('subscription_plan', css_class='form-group col-6 col-lg-2'),
                Column('subscription_price', css_class='form-group col-6 col-lg-2'), 
            ),
            Row(
                Column('email', css_class='form-group col-6 col-lg-4'),
                Column('phone_number', css_class='form-group col-6 col-lg-4'),
                Column('date', css_class='form-group col-6 col-lg-2'),
            ),
            Row(
                Column('street_address1', css_class='form-group col-6'),
            ),
            Row(
                Column('street_address2', css_class='form-group col-6'),
            ),
            Row(
                Column('town_or_city', css_class='form-group col-6 col-lg-4'),
                Column('postcode', css_class='form-group col-6 col-lg-2'),
            ),
            Row(
                Column('county', css_class='form-group col-6 col-lg-2'),
                Column('country', css_class='form-group col-6 col-lg-2'),
            )
        )
