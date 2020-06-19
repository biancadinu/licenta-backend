from rest_framework import serializers

from restapi import models


class UserFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserFood
        fields = ['food']
