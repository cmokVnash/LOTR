# Generated by Django 4.0 on 2022-01-11 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_remove_character_previous_character_relations'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='previous',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='quickstart.character'),
        ),
    ]
