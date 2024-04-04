from django.db import models
from django.contrib.auth.models import AbstractUser
from .static import users

class User(AbstractUser):
    photo=models.ImageField(upload_to="user_photos/", default='users/default.jpeg ')
    phone_number=models.CharField(max_length=13, unique=True, blank=True, null=True)
    friends=models.ManyToManyField('users.User', blank=True)


class FriendsRequest(models.Model):
    from_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    is_accepted=models.BooleanField(default=False)