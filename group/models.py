from django.db import models
from user.models import User


class GroupModel(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_groups')
    name = models.CharField(max_length=60, unique=True)
    image = models.ImageField(upload_to='group_main', null=True, blank=True)
    users = models.ManyToManyField(User, default=None, blank=True)

    @property
    def is_private(self):
        return self.private


class GroupWorkModel(models.Model):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='works')
    name = models.CharField(max_length=200, default='Noname work')
    photo = models.ImageField(upload_to='user_works')
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
