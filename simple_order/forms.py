from django import forms

from simple_product.models import Massage


class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = '__all__'

