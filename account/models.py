from django.db import models
from user.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='user_profile_photo')


class UserWorkModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    work_name = models.CharField(max_length=200, default='Noname work')
    photo = models.ImageField(upload_to='user_works')
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.pk)

    @property
    def num_likes(self):
        return self.liked.all().count()

    @property
    def get_tags(self):
        return self.tags.all()

    class Meta:
        ordering = ['-created']


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    work = models.ForeignKey(UserWorkModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created = models.DateTimeField(auto_now=True)