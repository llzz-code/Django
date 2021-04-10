from django.db import models

# Create your models here.
from django.db.models import Q

from mainapp.models import UserEntity, FruitEntity


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间',
                                       auto_now_add=True)
    last_time = models.DateTimeField(verbose_name='更新时间',
                                     auto_now=True)
    class Meta:
        abstract = True

class OrderManager(models.Manager):
    """
    QuerySet子类
    屏蔽取消的订单
    """
    def get_queryset(self):
        return super().get_queryset().filter(~Q(pay_status=5))

# 订单模型
class OrderEntity(BaseModel):
    num = models.CharField(max_length=20,
                           primary_key=True,
                           verbose_name='订单号')
    title = models.CharField(max_length=100,
                             verbose_name='订单名')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='订单金额')
    pay_type = models.IntegerField(choices=((0, '余额'),
                                            (1, '银行卡'),
                                            (2, '微信支付'),
                                            (3, '支付宝')),
                                   default=0,
                                   verbose_name='支付方式')
    pay_status = models.IntegerField(choices=((0, '待支付'),
                                              (1, '已支付'),
                                              (2, '待收货'),
                                              (3, '已收货'),
                                              (4, '完成'),
                                              (5, '取消')),
                                     default=0,
                                     verbose_name='订单状态')
    receiver = models.CharField(verbose_name='收货人',
                                max_length=20)
    receiver_phone = models.CharField(max_length=11,
                                      verbose_name='收货人手机')
    receiver_address = models.CharField(max_length=50,
                                        verbose_name='收货地址')

    objects = OrderManager()    # 显性创建objects

    def __str__(self):
        return self.title
    class Meta:
        db_table = 't_order'
        verbose_name = verbose_name_plural = '订单表'


# 购物车模型
class CartEntity(models.Model):
    class Meta:
        db_table = 't_cart'
        verbose_name = verbose_name_plural = '购物车表'

    user = models.OneToOneField(UserEntity,
                                on_delete=models.CASCADE,
                                verbose_name='账号')
    no = models.CharField(primary_key=True,
                          max_length=10,
                          verbose_name='购物车编号')
    def __str__(self):
        return self.no

# 声明水果商品与购物车的关系
class FruitCartEntity(models.Model):
    cart = models.ForeignKey(CartEntity,
                             on_delete=models.CASCADE,
                             verbose_name='购物车')
    fruit = models.ForeignKey(FruitEntity,
                              on_delete=models.CASCADE,
                              verbose_name='水果名')
    cnt = models.IntegerField(verbose_name='数量',
                              default=1)
    @property
    def price(self):
        return round(self.cnt*self.fruit.price, 2)
    def __str__(self):
        return self.fruit.name + ':' + self.cart.no

    class Meta:
        db_table = 't_fruit_cart'
        verbose_name = verbose_name_plural = '购物车详情表'