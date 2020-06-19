from rest_framework import serializers

from restapi import models


class DailyFoodSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)

    class Meta:
        model = models.DailyFoodList
        fields = '__all__'
        extra_kwargs = {
            'total_iron': {
                'read_only': True,
            }
        }
        depth = 1
