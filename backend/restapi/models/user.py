from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SEXES = [
        ('MALE', 'M'),
        ('FEMALE', 'F'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    iron_intake = models.IntegerField(blank=True, null=True)
    sex = models.CharField(choices=SEXES, max_length=10)
    age = models.IntegerField(blank=True, null=True)
