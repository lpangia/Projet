# Generated by Django 3.2.9 on 2021-12-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projet', '0002_alter_receipe_photo_alter_receipe_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
