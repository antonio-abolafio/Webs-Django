# Generated by Django 5.0.1 on 2024-01-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
