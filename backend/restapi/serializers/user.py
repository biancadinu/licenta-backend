from rest_framework import serializers
from rest_framework_jwt.serializers import User

from restapi import models


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['iron_intake']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

    def save(self, **kwargs):
        User.objects.create_user(username=self.validated_data['username'], password=self.validated_data['password'],
                                 first_name=self.validated_data['first_name'],
                                 last_name=self.validated_data['last_name'], email=self.validated_data['email'],)
