# Generated by Django 5.0.1 on 2024-06-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_alter_statistic_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
