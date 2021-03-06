from django.core import exceptions
from rest_framework import generics, permissions, views

from restapi import serializers, models


class RecipeGet(generics.RetrieveAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all()


class RecipeList(generics.ListAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class RecipeCreate(generics.CreateAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all()
    permission_classes = [permissions.IsAuthenticated]
