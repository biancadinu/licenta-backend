from rest_framework import serializers

from restapi import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['iron_intake']