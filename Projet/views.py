from django.http import HttpResponse
from Projet.models import Receipe
from django.shortcuts import render, redirect
from Projet.forms import RecipeForm, SearchRecipeForm


def index(request):
    recipes = Receipe.objects.all()
    if request.method == 'POST':
        form = SearchRecipeForm(request.POST)
        if form.is_valid():
            recipes = Receipe.objects.filter(title__icontains=form.cleaned_data.get('name'))
    else:
        form = SearchRecipeForm()
    return render(request, "Index.html", {"recipes": recipes, 'form': form})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})

