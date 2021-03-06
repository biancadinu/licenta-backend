from rest_framework import generics, permissions, response

from restapi import models, serializers


class UserUpdateView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        user.iron_intake = request.data['iron_intake']
        user.save()
        return response.Response(data={"message": "User updated"})


class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserCreateSerializer
    permission_classes = []


class UserDetailsView(generics.ListAPIView):
    serializer_class = serializers.UserCreateSerializer

    def get_queryset(self):
        return models.User.objects.filter(id=self.request.user.id)
