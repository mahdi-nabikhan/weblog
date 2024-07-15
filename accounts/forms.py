from django import forms
from .models import *


class registerForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    email = forms.CharField(label='Email', widget=forms.TextInput())
    age = forms.CharField(label='Age', widget=forms.TextInput())
    phone = forms.CharField(label='Phone', widget=forms.TextInput())
    password2 = forms.CharField(label='<PASSWORD>', widget=forms.PasswordInput())
    bio = forms.CharField(label='Bio', widget=forms.TextInput())

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password


class loginForms(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
