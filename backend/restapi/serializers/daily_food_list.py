from rest_framework import serializers

from restapi import models


class DailyFoodSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)

    class Meta:
        model = models.DailyFoodList
        fields = '__all__'
        depth = 1
