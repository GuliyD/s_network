from django import forms


class CreateGroupForm(forms.Form):
    group_name = forms.CharField(max_length=60)