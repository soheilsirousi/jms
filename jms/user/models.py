from django.contrib.auth.models import AbstractUser
from django.db import models
from user.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone = models.CharField(_('phone number'), unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.phone