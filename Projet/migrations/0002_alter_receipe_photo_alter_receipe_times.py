# Generated by Django 4.0 on 2021-12-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='photo',
            field=models.ImageField(null=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='times',
            field=models.IntegerField(verbose_name='Temps de préparation en minutes'),
        ),
    ]
