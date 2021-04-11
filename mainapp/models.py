import re
import uuid

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import models


class UserManager(models.Manager):
    def update(self, **kwargs):
        password = kwargs.get('password', None)
        if password and len(password) < 50:
            kwargs['password'] = make_password(password)
        super().update(**kwargs)

class UserValidator:
    @classmethod
    def valid_phone(cls, value):
        if re.match(r'1[1-57-9]\d{9}', value):
            raise ValidationError('手机格式不正确')
        return True

# Create your models here.
# 客户
class UserEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='用户名')
    age = models.IntegerField(default=0,
                              verbose_name='年龄')
    phone = models.CharField(max_length=11,
                             verbose_name='手机号',
                             validators=[UserValidator.valid_phone],
                             blank=True,  # 站点表单可以为空
                             null=True)  # 数据库字段可以为空
    password = models.CharField(max_length=100,
                                verbose_name='密码',
                                blank=True,
                                null=True)
    objects = UserManager()
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.password) < 50:
            self.password = make_password(self.password)
        super().save()

    def __str__(self):
        return self.name

    class Meta:
        # 设置表名
        db_table = 'app_user'
        verbose_name = '客户管理'
        verbose_name_plural = verbose_name
        ordering = ('id',)

class RealProfile(models.Model):
    # 一对一关系表
    user = models.OneToOneField(UserEntity, verbose_name='账号',
                                on_delete=models.CASCADE)
    real_name = models.CharField(max_length=20,
                                 verbose_name='真实姓名')
    number = models.CharField(max_length=18,
                              verbose_name='证件号')
    real_type = models.IntegerField(verbose_name='证件类型',
                                    choices=((0, '身份证'),
                                             (1, '护照'),
                                             (2, '驾驶证')))
    image1 = models.ImageField(verbose_name='正面照',
                               upload_to='user/real')
    image2 = models.ImageField(verbose_name='反面照',
                               upload_to='user/real')

    def __str__(self):
        return self.real_name


    class Meta:
        db_table = 't_user_profile'
        verbose_name = verbose_name_plural = '实名认证表'




# 水果分类
class CateTypeEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='分类名')
    order_num = models.IntegerField(verbose_name='排序')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        ordering = ['-order_num']  # 设置排序字段，-表示降序
        verbose_name = '水果分类'
        verbose_name_plural = verbose_name


class StoreEntity(models.Model):
    # 默认情况下，模型会自动创建主键id字段--隐式
    # 但是也可以显示的方式声明主键(primary key)
    id = models.UUIDField(primary_key=True,
                          verbose_name='店号')
    name = models.CharField(max_length=50,
                            verbose_name='店名')
    # 表中对应字段type_
    store_type = models.IntegerField(choices=((0, '自营'), (1, '第三方')),
                                     verbose_name='店铺类型',
                                     db_column='type_')

    address = models.CharField(max_length=100,
                               verbose_name='地址')
    # 支持城市搜索,创建city索引
    city = models.CharField(max_length=50,
                            verbose_name='城市',
                            db_index=True)
    create_time = models.DateTimeField(verbose_name='成立时间',
                                       auto_now_add=True,
                                       null=True)
    last_time = models.DateTimeField(verbose_name='最后变更时间',
                                     auto_now=True,
                                     null=True)
    logo = models.ImageField(verbose_name='LOGO',
                             upload_to='store',
                             width_field='logo_width',
                             height_field='logo_height',
                             null=True,
                             blank=True)

    logo_width = models.IntegerField(verbose_name='LOGO宽',
                                     null=True)
    logo_height = models.IntegerField(verbose_name='LOGO高',
                                      null=True)
    summary = models.TextField(verbose_name='介绍',
                               blank=True,
                               null=True)
    opened = models.BooleanField(verbose_name='是否开业',
                                 default=False)

    def __str__(self):
        return self.name + '-' + self.city

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # 调用模型保存方法时被调用
        if not self.id:  # 判断是否为新增
            self.id = uuid.uuid4().hex
        super().save()

    @property
    def id_(self):
        # return str(self.id).replace('-', '')
        return self.id.hex

    class Meta:
        db_table = 't_store'
        verbose_name = '店铺'
        verbose_name_plural = verbose_name
        unique_together = (('name', 'city'),)
        ordering = ('create_time',)


class FruitEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='水果名')

    price = models.FloatField(verbose_name='价格')
    category = models.ForeignKey(CateTypeEntity,
                                 related_name='fruits',
                                 on_delete=models.CASCADE,
                                 to_field='id',
                                 verbose_name='所属类别')
    store_name = models.ForeignKey(StoreEntity,
                                   on_delete=models.CASCADE,
                                   verbose_name='所属店铺',
                                   null=True)

    source = models.CharField(max_length=30,
                              verbose_name='源产地')
    summary = models.TextField(verbose_name='介绍',
                               blank=True,
                               null=True)
    img = models.ImageField(verbose_name='水果图片',
                            upload_to='store',
                            width_field='img_width',
                            height_field='img_height',
                            null=True,
                            blank=True)

    img_width = models.IntegerField(verbose_name='水果图片宽',
                                    null=True)
    img_height = models.IntegerField(verbose_name='水果图片高',
                                     null=True)

    # 收藏表(集合)。第三张表，多对多关系，不需要实例,默认情况下，反向引用的名称是当前类的小写名称
    users = models.ManyToManyField(UserEntity,
                                   db_table='t_collect',
                                   related_name='fruits',
                                   verbose_name='收藏用户列表',
                                   blank=True,
                                   null=True)

    tags = models.ManyToManyField('TagEntity',
                                  db_table='t_fruit_tags',
                                  related_name='fruits',
                                  verbose_name='标签',
                                  blank=True,
                                  null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_fruit'
        verbose_name = '水果表'
        verbose_name_plural = verbose_name
        ordering = ('id',)


class TagEntity(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='标签名')
    order_num = models.IntegerField(verbose_name='排序',
                                    default=1)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_tag'
        verbose_name = verbose_name_plural = '标签表'
        ordering = ('-order_num',)

