# Generated by Django 3.2.9 on 2021-12-18 13:40

from django.db import migrations, models
import django.db.models.deletion

def add_category(apps, schemaeditor):
    RecipeCategory = apps.get_model("Projet", "RecipeCategory")
    RecipeCategory.objects.get_or_create(
        name='Entrées'
    )
    RecipeCategory.objects.get_or_create(
        name='Encas'
    )
    RecipeCategory.objects.get_or_create(
        name='Desserts'
    )
    RecipeCategory.objects.get_or_create(
        name='Plats'
    )



class Migration(migrations.Migration):

    dependencies = [
        ('Projet', '0004_auto_20211218_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='structures', to='Projet.recipecategory', verbose_name='category'),
        ),
        migrations.RunPython(add_category, lambda x, y: None),
    ]