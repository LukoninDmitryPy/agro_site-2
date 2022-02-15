from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

