# Generated by Django 5.0.1 on 2024-06-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_alter_statistic_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='players/', verbose_name='Perfil'),
        ),
    ]
