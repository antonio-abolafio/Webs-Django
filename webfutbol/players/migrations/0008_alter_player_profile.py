# Generated by Django 5.0.1 on 2024-06-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_player_alias_alter_player_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile',
            field=models.ImageField(blank=True, default='usuario.png', null=True, upload_to='players/', verbose_name='Perfil'),
        ),
    ]
