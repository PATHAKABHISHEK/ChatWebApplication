from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'firstname',
            'lastname',
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname  = self.cleaned_data['lastname']
        user.username  = self.cleaned_data['username']
        user.email   = self.cleaned_data['email']

        if commit:
            user.save()
            return user
