# Generated by Django 4.1.7 on 2023-03-07 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_cars_goods_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='Goods_name',
        ),
    ]
