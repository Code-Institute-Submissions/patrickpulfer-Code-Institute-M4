# Generated by Django 3.2.8 on 2021-10-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
