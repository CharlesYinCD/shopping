from django.db import models

# Create your models here.

from user.models import Users
from utils.base_model import BaseModel


class Orders(BaseModel):
    Goods_name = models.CharField(max_length=200)
    goods_number= models.IntegerField(max_length=100)
    order_price = models.IntegerField(max_length=100)
    address = models.TextField(max_length=100)
    user = models.ForeignKey(Users, related_name="user_orders", on_delete=models.CASCADE)
    class Meta:
        db_table = 'orders'
        verbose_name = 'orders'
        verbose_name_plural = 'orders'