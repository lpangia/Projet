from django.db import models


class Receipe(models.Model):
    title = models.CharField(null=False, max_length=100)
    photo = models.ImageField(upload_to="pictures/", null=True, blank=True)
    ingredients = models.TextField(null=False)
    times = models.IntegerField(null=False, verbose_name="Temps de préparation en minutes")
    guide = models.TextField(null=False)

    class Meta:
        verbose_name = "Recette"
        ordering = ("title",)

    def __str__(self):
        return self.title
