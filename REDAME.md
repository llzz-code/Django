```shell script
pip install django==2.0.1
```

```
helloDjango
    |--- helloDjango    主工程目录
            |--- settings.py    # 设置文件，数据库连接、app注册、中间件及模板配置
            |--- urls.py        # 总路由
            |--- wsgi.py        # Django实现wsgi的脚本
            |--- __init__.py    
    |--- mainapp        应用模块(主)
            |--- __init__.py
            |--- admin.py       # 后台管理配置脚本
            |--- models.py      # 数据模型类声明所在脚本
            |--- view.py        # 声明当前应用的视图处理函数或类
            |--- urls.py        # 自己增加的当前应用模块的子路由
            |--- tests.py       # 当前应用模块的单元测试类
            |--- apps.py        # 声明当前应用的基本信息
    |--- manage.py      WEB应用的启动脚本，项目工程的入口
```

```cmd
python manage.py runserver
```

```python
# 请求头
# request.get_full_path()
# request.path
# request.method
# request.path_info
# request.content_type
# 请求体   
# request.body
# 字典类型    
# request.COOKIES
# request.GET
# request.POST
# redirect重定向
```

```shell script
python manage.py createsuperuser
```

> 数据库连接与ORM模型

默认是sqlite3数据库，需先生成迁移文件
```shell script
python manage.py makemigrations

```
开始迁移
```shell script
python manage.py migrate
```

admin
llz200515
2270038123@qq.com

```python
# Fruit 水果模型类(name, price, source, cate_type_id)
# FruitImage 水果图片(fruit_id, url, width, height, name)
# CateType 水果分类(name, order_num)
```

```python
FruitEntity.objects.raw('select name, price from t_fruit where price<10')


主表中获取从表的数据
login_url = UserEntity.objects.get(pk=1)
# 以隐性方式，读取从表的数据：对象.关联模型类全小写名称.属性
login_url.realprofile.number
```
```python
# 查看水果被哪些用户收藏
fruit = FruitEntity.objects.get(pk=1)
fruit.users.all()
# 同款推荐
cate1 = CateTypeEntity.objects.get(pk=1)
cate1.fruits.values()
```

#### 模板加载对象
* 1、加载
```python
template = loader.get_template('index.html')
```

* 渲染
```python
html = template.render(context)    # context是一个dict类型对象
```

![]()![2SJFEE55JQ0ZA7IUMRW@}%C](D:\python\hiDjango\helloDjango\static\images\2SJFEE55JQ0ZA7IUMRW@}%C.png)