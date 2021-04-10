# Generated by Django 2.0.1 on 2021-04-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('num', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='订单号')),
                ('title', models.CharField(max_length=100, verbose_name='订单名')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单金额')),
                ('pay_type', models.IntegerField(choices=[(0, '余额'), (1, '银行卡'), (2, '微信支付'), (3, '支付宝')], default=0, verbose_name='支付方式')),
                ('pay_status', models.IntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '待收货'), (3, '已收货'), (4, '完成'), (5, '取消')], default=0, verbose_name='订单状态')),
                ('receiver', models.CharField(max_length=20, verbose_name='收货人')),
                ('receiver_phone', models.CharField(max_length=11, verbose_name='收货人手机')),
                ('receiver_address', models.CharField(max_length=50, verbose_name='收货地址')),
            ],
            options={
                'verbose_name': '订单表',
                'verbose_name_plural': '订单表',
                'db_table': 't_order',
            },
        ),
    ]
