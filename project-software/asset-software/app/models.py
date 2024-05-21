
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Users

# Create your models here.

class Asset(models.Model):
    assetName = models.TextField()
    assetId = models.CharField(max_length=200)
    assignDate = models.DateTimeField(verbose_name="assign date", auto_now_add=True)
    assetImage = models.ImageField(upload_to='picture')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    
    def __str__(self):
        return self.assetName
