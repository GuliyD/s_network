from django.db import models
from user.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='user_profile_photo')


class UserWorkModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    photo = models.ImageField(upload_to='user_works')