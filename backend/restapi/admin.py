from django.contrib import admin
from django.contrib.auth.models import User

from restapi import models
admin.site.register(models.User)
admin.site.register(models.Food)
admin.site.register(models.DailyFoodList)
admin.site.register(models.Recipe)
admin.site.register(models.Ingredient)
admin.site.register(models.UserRecipe)

