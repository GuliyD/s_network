from django import forms
from user.models import User
from .models import ProfileModel


class WorkForm(forms.Form):
    work_name = forms.CharField(max_length=200, required=False)
    photo = forms.ImageField()


class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['photo']


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)