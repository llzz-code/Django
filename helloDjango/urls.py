"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path, include

from mainapp.fruit.views import fruit_list


def index(request: HttpRequest):

    # 加载数据模型
    users = [
        {'id': 1, 'name': 'lz'},
        {'id': 2, 'name': 'zhangsan' }
    ]

    # return HttpResponse('<h1>hi,django</h1>'.encode('utf-8'))
    # 将数据渲染到模板中，并将渲染之后html响应给客户端
    return render(request, 'index.html', {'users': users,
                                          'msg': '所有用户'})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    # include()导入app模块下urls中声明的所有子路由
    path('user/', include('mainapp.user.urls')),
    path('', fruit_list)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path('fruit/', include('mainapp.fruit.urls')),