from django.db import models
# Create your models here.
from user.models import Users
from utils.base_model import BaseModel


class Cars(BaseModel):
    Goods_name = models.CharField(max_length=200)
    goods_number = models.IntegerField(max_length=100)
    user = models.ForeignKey(Users, related_name="user_car", on_delete=models.CASCADE)

    class Meta:
        db_table = "cars"
        verbose_name = 'cars'
        verbose_name_plural = 'cars'
