from rest_framework.test import APITestCase

from restapi import models


class BaseTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.common_password = 'Passw0rd!'
        cls.superuser = models.User.objects.create_superuser(username='superuser', password=cls.common_password,
                                                             first_name="Super", last_name="User",
                                                             email="superuser@email.com")
        cls.normal_user = models.User.objects.create_user(username='normal_user', password=cls.common_password,
                                                          first_name="Normal", last_name="User",
                                                          email="normal_user@email.com")
        cls.recipe_data = {
            'name': 'recipe_1',
            'description': 'test',
            'duration': '15',
            'portion': '2',
            'pictures': '',
            'total_iron': '2.5'
        }
        cls.recipe_1 = models.Recipe.objects.create(**cls.recipe_data)
        cls.recipe_data['name'] = 'recipe_2'
        cls.recipe_2 = models.Recipe.objects.create(**cls.recipe_data)
