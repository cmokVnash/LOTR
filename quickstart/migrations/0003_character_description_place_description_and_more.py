# Generated by Django 4.0 on 2022-01-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_remove_region_place_place_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]