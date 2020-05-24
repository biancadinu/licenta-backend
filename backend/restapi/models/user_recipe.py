from django.db import models


class UserRecipe(models.Model):
    user = models.ForeignKey("restapi.User", on_delete=models.CASCADE)
    recipe = models.ForeignKey("restapi.Recipe", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()