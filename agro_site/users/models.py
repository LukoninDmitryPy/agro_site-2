from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Group

class MyUser(AbstractUser):
    username = models.CharField(max_length=30,
        unique=True,
    )
    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        blank=True
    )
    adress = models.TextField(
        max_length=100,
        blank=True
    )
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    is_seller = models.BooleanField(default=False)

