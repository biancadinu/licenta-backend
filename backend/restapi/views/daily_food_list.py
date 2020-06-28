from rest_framework import generics, response, status

from restapi import models, serializers


class DailyFoodListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.DailyFoodSerializer
    queryset = models.DailyFoodList.objects.all()

    def list(self, request, *args, **kwargs):
        user = self.request.user
        date = request.query_params['date']
        self.queryset = models.DailyFoodList.objects.filter(date=date, user=user)
        resp = super().list(request, *args, **kwargs)
        total_iron = 0
        for daily_food_list in self.queryset:
            total_iron += daily_food_list.food.all()[0].iron
        resp.data[0]['total_iron'] = total_iron
        return response.Response(data=resp.data)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        list = models.DailyFoodList.objects.create(user=user, servings=self.request.data['servings'])
        list.food.add(models.Food.objects.get(id=self.request.data['food']))
        list.save()
        return response.Response(data={'message': 'da'}, status=status.HTTP_200_OK)


class DailyFoodDelete(generics.DestroyAPIView):
    serializer_class = serializers.DailyFoodSerializer
    queryset = models.DailyFoodList.objects.all()


class DailyFoodUpdate(generics.UpdateAPIView):
    serializer_class = serializers.DailyFoodSerializer
    queryset = models.DailyFoodList.objects.all()
