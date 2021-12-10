from django.db import models


class Receipe(models.Model):
    title = models.CharField(null=False, max_length=100)
    photo = models.ImageField(upload_to="pictures/")
    ingredients = models.TextField(null=False)
    times = models.TimeField(null=False, auto_now=False, auto_now_add=False)
    guide = models.TextField(null=False)

    class Meta:
        verbose_name = "Recette"
        ordering = ("title",)

    def __str__(self):
        return self.title
