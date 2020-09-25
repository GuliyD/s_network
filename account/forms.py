from django import forms
from user.models import User
from .models import ProfileModel


class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['photo']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)