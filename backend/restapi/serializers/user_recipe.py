from rest_framework import serializers

from restapi import models


class UserRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRecipe
        fields = ['recipe', 'rating']
