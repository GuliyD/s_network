# Generated by Django 3.1.1 on 2020-09-25 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userworkmodel',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userworkmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.userworkmodel'),
        ),
    ]
