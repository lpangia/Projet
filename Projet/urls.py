"""Projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Projet import settings
from Projet.views import index, create_recipe, recipe_list, register, my_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home', index, name='index'),
    path('recipe/create', create_recipe, name='create_recipe'),
    path('recipe_list/<name>', recipe_list, name='recipe_list'),
    path('my_recipe', my_recipe, name='my_recipe'),
    path("register/", register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
