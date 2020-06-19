"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from restapi import views

from backend import settings

api_urlpatterns = [
    path('food/', views.FoodListCreateView.as_view()),
    path('daily-food-list/', views.DailyFoodListCreate.as_view()),
    path('daily-food-list/<int:pk>', views.DailyFoodDelete.as_view()),
    path('recipe/', views.RecipeList.as_view()),
    path('recipe/<int:pk>', views.RecipeGet.as_view()),
    path('recipe/<int:pk>/favorite/', views.UserRecipeView.as_view()),
    path('recipe/<int:pk>/remove-favorite/', views.UserRecipeDelteView.as_view()),
    path('food/<int:pk>/favorite/', views.UserFoodView.as_view()),
    path('food/<int:pk>/remove-favorite/', views.UserFoodDeleteView.as_view()),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path(r'auth/', obtain_jwt_token),
    path(r'token-refresh/', refresh_jwt_token),
    path(r'users/', views.UserUpdateView.as_view()),
    path(r'register/', views.UserCreateView.as_view())
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
