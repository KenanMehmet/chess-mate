from django import forms
from django.core.exceptions import ValidationError

from .models import *

class PlayerSignupForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(PlayerSignupForm, self).clean()
        password_conf = cleaned_data.get("password_conf")
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")

        existing_client = Player.objects.filter(email__iexact=email).first()
        if existing_client:
            raise ValidationError("Email already in use")

        if password != password_conf:
            raise ValidationError("Passwords do not match")

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    password_conf = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Player
        fields = [
            "username",
            "email",
            "password",
            "nationality"
        ]
