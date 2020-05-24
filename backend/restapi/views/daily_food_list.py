import datetime

from django.core import exceptions
from rest_framework import generics, response, status

from restapi import models, serializers


class DailyFoodListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.DailyFoodSerializer
    queryset = models.DailyFoodList.objects.all()


class DailyFoodUpdate(generics.UpdateAPIView):
    serializer_class = serializers.DailyFoodSerializer
    queryset = models.DailyFoodList.objects.all()
