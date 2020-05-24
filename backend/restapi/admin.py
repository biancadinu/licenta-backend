from django.contrib import admin

from restapi import models

admin.site.register(models.User)
admin.site.register(models.Food)
admin.site.register(models.DailyFoodList)

