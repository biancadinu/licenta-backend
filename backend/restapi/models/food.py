from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=40)
    iron = models.FloatField()
    calories = models.IntegerField()
    serving_size_amount = models.FloatField()
    serving_size_unit = models.CharField(max_length=10)
    total_fat = models.PositiveSmallIntegerField(default=0)
    saturated_fat = models.PositiveSmallIntegerField(default=0)
    trans_fat = models.PositiveSmallIntegerField(default=0)
    cholesterol = models.PositiveSmallIntegerField(default=0)
    sodium = models.PositiveSmallIntegerField(default=0)
    total_carbs = models.PositiveSmallIntegerField(default=0)
    fiber = models.PositiveSmallIntegerField(default=0)
    sugars = models.PositiveSmallIntegerField(default=0)
    protein = models.PositiveSmallIntegerField(default=0)
    vitamin_a = models.PositiveSmallIntegerField(default=0)
    vitamin_c = models.PositiveSmallIntegerField(default=0)
    calcium = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
