# Generated by Django 3.2.8 on 2021-10-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20211015_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='forum_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
