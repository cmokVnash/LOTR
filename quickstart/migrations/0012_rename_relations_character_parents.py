# Generated by Django 4.0 on 2022-01-11 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_character_previous'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='relations',
            new_name='parents',
        ),
    ]
