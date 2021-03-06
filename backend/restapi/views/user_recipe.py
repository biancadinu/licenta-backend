from django.core import exceptions
from rest_framework import generics, permissions, response, status

from restapi import models, serializers


class UserRecipeView(generics.CreateAPIView):
    queryset = models.UserRecipe.objects.all()
    serializer_class = serializers.UserRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        try:
            recipe = models.Recipe.objects.get(id=self.kwargs['pk'])
        except exceptions.ObjectDoesNotExist:
            pass
        else:
            models.UserRecipe.objects.create(user=user, recipe=recipe)
            return response.Response(data={}, status=status.HTTP_200_OK)


class UserRecipeDelteView(generics.DestroyAPIView):
    queryset = models.UserRecipe.objects.all()
    serializer_class = serializers.UserRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        try:
            recipe = models.Recipe.objects.get(id=self.kwargs['pk'])
        except exceptions.ObjectDoesNotExist:
            pass
        else:
            models.UserRecipe.objects.get(user=user, recipe=recipe).delete()
            return response.Response(data={}, status=status.HTTP_200_OK)
