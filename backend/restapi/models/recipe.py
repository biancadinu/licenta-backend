from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey('restapi.Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5048)
    duration = models.IntegerField(help_text="in min")
    portion = models.CharField(help_text="how many portions are in this recipe", max_length=40)
    pictures = models.ImageField(upload_to='images/recipes')
    total_iron = models.FloatField()
    ingredients = models.TextField(max_length=2048, null=True)

    def __str__(self):
        return self.name