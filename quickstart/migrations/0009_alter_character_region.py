# Generated by Django 4.0 on 2022-01-11 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_alter_character_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.region'),
        ),
    ]
