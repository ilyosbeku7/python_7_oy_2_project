from django.db import models
from django.contrib.auth.models import AbstractUser
from .static import users

class User(AbstractUser):
    photo=models.ImageField(upload_to="user_photos/", default='users/default.jpeg ')
    phone_number=models.CharField(max_length=13, unique=True, blank=True, null=True)