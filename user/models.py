from django.db import models
# Create your models here.
from utils.base_model import BaseModel


class Users(BaseModel):
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    class Meta:
        db_table = 'users'
        verbose_name = 'users'
        verbose_name_plural = 'users'