from django import forms
from django.core.validators import RegexValidator


class BikeForm(forms.Form):
    _type = forms.CharField(min_length=2, max_length=2, validators=[RegexValidator(r'^(MN|HB|RD)$')], required=True)
    model = forms.CharField(min_length=1, max_length=255, required=True)
    headline = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 30}), required=True)
    size = forms.IntegerField(min_value=12, max_value=30, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    image = forms.FileField(required=True)
