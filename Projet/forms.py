from django import forms
from django.forms import ModelForm
from Projet.models import Receipe


class RecipeForm(ModelForm):
    class Meta:
        model = Receipe
        fields = ['title', 'photo', 'ingredients', 'times', 'guide']


class SearchRecipeForm(forms.Form):
    name = forms.CharField(label='Rechercher une recette', max_length=100, required=False)