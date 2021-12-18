from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Projet.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'photo', 'category', 'ingredients', 'times', 'guide']


class SearchRecipeForm(forms.Form):
    name = forms.CharField(label='Rechercher une recette', max_length=100, required=False)


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]