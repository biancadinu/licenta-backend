from django.db import models


class Rating(models.Model):
    user = models.ForeignKey("restapi.User", on_delete=models.CASCADE)
    recipe = models.ForeignKey("restapi.Food", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0)
