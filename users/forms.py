from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email']
