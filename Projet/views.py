from django.http import HttpResponse
from Projet.models import Receipe
from django.shortcuts import render


def index(request):
    recipes = Receipe.objects.all()
    return render(request, "index.html", {"recipes": recipes})
