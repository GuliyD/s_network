# Generated by Django 3.1.1 on 2020-09-23 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200923_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userworkmodel',
            options={'ordering': ['-created']},
        ),
    ]
