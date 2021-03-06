from django.core import exceptions
from rest_framework import serializers

from restapi import models


class RecipeSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField(read_only=True, default=False)

    class Meta:
        model = models.Recipe
        fields = ['id', 'name', 'description', 'duration', 'portion', 'pictures', 'total_iron', 'is_favorite',
                  'ingredients']
        extra_kwargs = {
            'pictures': {
                'read_only': True
            }
        }

    def get_is_favorite(self, recipe):
        user = self.context['request'].user
        try:
            user_recipes = models.UserRecipe.objects.get(user=user, recipe=recipe)
        except exceptions.ObjectDoesNotExist:
            return False
        else:
            if recipe.id == user_recipes.recipe.id:
                return True
        return False
