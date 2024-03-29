# Generated by Django 4.1.7 on 2023-03-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Goods_name', models.CharField(max_length=200)),
                ('Goods_price', models.IntegerField(max_length=100)),
                ('Goods_type', models.SmallIntegerField(choices=[(1, '日用百货'), (2, '服装鞋帽'), (3, '通讯数码'), (4, '美容产品'), (5, '书籍音像'), (6, '家用电器'), (7, '食品'), (8, '文体用品')])),
                ('car', models.ManyToManyField(to='car.cars')),
                ('order', models.ManyToManyField(to='order.orders')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]
