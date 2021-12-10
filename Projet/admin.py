from django.contrib import admin
from django.contrib.admin import ModelAdmin


from Projet.models import Receipe


class ReceipeAdmin(ModelAdmin):
    list_display = ["title", "times"]


admin.site.register(Receipe, ReceipeAdmin)
