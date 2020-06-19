from django.db import models


class UserFood(models.Model):
    user = models.ForeignKey("restapi.User", on_delete=models.CASCADE)
    food = models.ForeignKey("restapi.Food", on_delete=models.CASCADE)
