from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']