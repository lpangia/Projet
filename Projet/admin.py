from django.contrib import admin
from django.contrib.admin import ModelAdmin


from Projet.models import Recipe, RecipeCategory


class RecipeAdmin(ModelAdmin):
    list_display = ["title", "times", "category", "user"]


class RecipeCategoryAdmin(ModelAdmin):
    list_display = ["name"]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
