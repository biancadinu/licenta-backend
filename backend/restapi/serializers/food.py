from django.core import exceptions
from rest_framework import serializers

from restapi import models


class FoodSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField(read_only=True, default=False)

    def get_is_favorite(self, recipe):
        user = self.context['request'].user
        try:
            user_food = models.UserFood.objects.get(user=user)
        except exceptions.ObjectDoesNotExist:
            return False
        else:
            if user_food.id == user_food.id:
                return True
        return False

    class Meta:
        model = models.Food
        fields = "__all__"
