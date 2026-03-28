from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telegram_id = models.CharField(max_length=255, blank=True, null=True)
    telegram_username = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    