from rest_framework import serializers

from restapi import models


class DailyFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyFoodList
        fields = '__all__'
        extra_kwargs = {
            'total_iron': {
                'read_only': True,
            }
        }