from django.db import models


class DailyFoodList(models.Model):
    user = models.ForeignKey('restapi.User', on_delete=models.CASCADE)
    food = models.ManyToManyField('restapi.Food')
    servings = models.IntegerField()
    date = models.DateField(auto_now=True)
