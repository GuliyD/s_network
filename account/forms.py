from django import forms
from user.models import User


class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_photo']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)