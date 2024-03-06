from django import forms
from users.models import CustomUser


class TestviyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("first_name", "phone_number", "phone_number2", "password")


