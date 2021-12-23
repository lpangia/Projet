from django.http import HttpResponse
from Projet.models import Recipe
from django.shortcuts import render, redirect
from Projet.forms import RecipeForm, SearchRecipeForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login


def index(request):
    recipes = Recipe.objects.all()
    if request.method == 'POST':
        form = SearchRecipeForm(request.POST)
        if form.is_valid():
            recipes = Recipe.objects.filter(title__icontains=form.cleaned_data.get('name'))
    else:
        form = SearchRecipeForm()
    return render(request, "Index.html", {"recipes": recipes, 'form': form})


def recipe_list(request, name):
    recipes = Recipe.objects.filter(category__name=name)
    return render(request, "recipes.html", {"recipes": recipes})


def my_recipe(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, "recipes.html", {"recipes": recipes})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            recipe.user = request.user
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    return render(request, "registration/register.html", {"form": form})

