from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from . manager import UserManager
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16, unique=True)

    email_token = models.CharField(max_length=24, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    is_varified = models.BooleanField(default=False)

    object = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username