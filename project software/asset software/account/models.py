
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Users(AbstractUser):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    block = models.BooleanField(default=False)
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='picture')
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=500, default='empty')

    def __str__(self):
        return self.username
