# Generated by Django 5.0.1 on 2024-06-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_alter_team_shield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='shield',
            field=models.ImageField(default='shields/escudo_vacio.jpg', upload_to='shields/', verbose_name='Escudo'),
        ),
    ]
