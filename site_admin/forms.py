from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from guitars.models import Guitar, Category


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
                Column('category', css_class='form-group col-2'),
                Column('brand', css_class='form-group col-2'),
                Column('guitar_model', css_class='form-group col-2'),
                Column('tier', css_class='form-group col-2'),
                Column('image_id', css_class='form-group col-4'),
            ),
            Row(
                Column('status', css_class='form-group col-2'),
                Column('handed', css_class='form-group col-2'),
                Column('condition', css_class='form-group col-2'),
                Column('rating_condition', css_class='form-group col-2'),
                Column('rating_overall', css_class='form-group col-2'),
                Column('featured', css_class='form-group col-2 mb-0 d-flex align-items-end'),
            ),
            Row(
                Column('no_strings', css_class='form-group col-2'),
                Column('approx_age_years', css_class='form-group col-2'),
                Column('tuners', css_class='form-group col-2'),
                Column('frets', css_class='form-group col-2'),
                Column('no_pickups', css_class='form-group col-2'),
                Column('controls', css_class='form-group col-2'),
            ),
            Row(
                Column('construction', css_class='form-group col-2'),
                Column('body_wood', css_class='form-group col-2'),
                Column('body_top', css_class='form-group col-2'),
                Column('neck_wood', css_class='form-group col-2'),
                Column('neck_profile', css_class='form-group col-2'),
            ),
            Row (
                Column('pickups_desc', css_class='form-group col-5'),
                Column('owners_additional_comments', css_class='form-group col-5'),
                Column('favourites', css_class='form-group col-2'),
            ),
        )

        
        
        
        
        
        
        
         
        
        
        
        
        
        
        
        