from django.db import models
from django.contrib.auth.models import AbstractUser

from authentication.managers import CustomUserManager

# Create your models here.

class UserModel(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(null=True, blank=True, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    ordering = ('email',)

    objects = CustomUserManager()

    def get_username(self):
        return self.email