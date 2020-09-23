from django.db import models
from user.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='user_profile_photo')


LIKE_CHOICES = [
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
]


class UserWorkModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    photo_name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='user_works')
    created = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
    like_value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.pk)

    @property
    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        ordering = ['-created']


class CommentModel(models.Model):
    work = models.ForeignKey(UserWorkModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created = models.DateTimeField(auto_now=True)