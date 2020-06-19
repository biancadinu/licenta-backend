from django.core import exceptions
from rest_framework import generics, permissions, response, status

from restapi import models, serializers


class UserFoodView(generics.CreateAPIView):
    queryset = models.UserFood.objects.all()
    serializer_class = serializers.UserFoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        try:
            food = models.Food.objects.get(id=self.kwargs['pk'])
        except exceptions.ObjectDoesNotExist:
            pass
        else:
            models.UserFood.objects.create(user=user, food=food)
            return response.Response(data={}, status=status.HTTP_200_OK)


class UserFoodDeleteView(generics.DestroyAPIView):
    queryset = models.UserFood.objects.all()
    serializer_class = serializers.UserFoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        try:
            food = models.Food.objects.get(id=self.kwargs['pk'])
        except exceptions.ObjectDoesNotExist:
            pass
        else:
            models.UserFood.objects.get(user=user, food=food).delete()
            return response.Response(data={}, status=status.HTTP_200_OK)
