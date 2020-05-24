from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=40)
    iron = models.FloatField()
    calories = models.IntegerField()
    serving_size_amount = models.FloatField()
    serving_size_unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name