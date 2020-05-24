from rest_framework import generics, filters

from restapi import serializers, models


class FoodListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.FoodSerializer
    # permission_classes = #ToDo
    queryset = models.Food.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']