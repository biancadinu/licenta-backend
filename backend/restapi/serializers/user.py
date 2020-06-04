from rest_framework import serializers

from restapi import models


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['iron_intake']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
