from django import forms
from django.core.exceptions import ValidationError
#from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    phone = forms.CharField()
    required_css_class = 'form-group'

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'delivery', 'address',  'city']


    def as_div(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<div%(html_class_attr)s><strong>%(label)s</strong><br/> %(field)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    def clean(self):
        if self.cleaned_data['delivery'] and self.cleaned_data['address'] is None:
            raise ValidationError('Выберите самовывоз либо укажите адрес')