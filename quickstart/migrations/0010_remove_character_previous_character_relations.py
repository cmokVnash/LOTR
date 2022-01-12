# Generated by Django 4.0 on 2022-01-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_alter_character_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='previous',
        ),
        migrations.AddField(
            model_name='character',
            name='relations',
            field=models.ManyToManyField(to='quickstart.Character'),
        ),
    ]
