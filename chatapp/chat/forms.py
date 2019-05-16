from django import forms
from .models import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name  = forms.CharField(max_length=100)
    user_name  = forms.CharField(max_length=100)
    email_id   = forms.CharField(max_length=100)
    password   = forms.CharField(max_length=100)
