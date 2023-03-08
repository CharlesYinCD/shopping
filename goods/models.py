from django.db import models
from car.models import Cars
from order.models import Orders
from utils.base_model import BaseModel


class Goods(BaseModel):
    Goods_name = models.CharField(max_length=200)
    Goods_price = models.IntegerField(max_length=100)
    Goods_type = models.SmallIntegerField(choices=((1, "日用百货"), (2, "服装鞋帽"), (3, "通讯数码"),(4,"美容产品"),
                                                   (5,"书籍音像"),(6,'家用电器'),(7,"食品"),(8,"文体用品")))
    order= models.ManyToManyField(to=Orders)
    car= models.ManyToManyField(to=Cars)

    class Meta:
        db_table = "goods"
        verbose_name = 'goods'
        verbose_name_plural = 'goods'