# Generated by Django 3.1.1 on 2020-09-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userworkmodel_like_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='userworkmodel',
            name='work_name',
            field=models.CharField(default='Noname work', max_length=200),
        ),
        migrations.AlterField(
            model_name='userworkmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
