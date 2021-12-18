from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Recipe(models.Model):
    title = models.CharField(null=False, max_length=100)
    photo = models.ImageField(upload_to="pictures/", null=True, blank=True)
    ingredients = models.TextField(null=False)
    times = models.IntegerField(null=False, verbose_name="Temps de préparation en minutes")
    guide = models.TextField(null=False)
    category = models.ForeignKey(
        "RecipeCategory",
        related_name="structures",
        on_delete=models.PROTECT,
        verbose_name='category',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        default = 1,
        null = True,
        on_delete = models.SET_NULL
    )

    class Meta:
        verbose_name = "Recette"
        ordering = ("title",)

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        verbose_name = "Category de recette"
        ordering = ("name",)

    def __str__(self):
        return self.name

