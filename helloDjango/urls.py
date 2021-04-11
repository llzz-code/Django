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
from django.conf.urls import url
from django.conf.urls.static import static as st
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path, include
from django.views import static

from mainapp.fruit.views import fruit_list


def index(request: HttpRequest):
    return render(request, 'index.html', locals())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    # include()导入app模块下urls中声明的所有子路由
    path('user/', include('mainapp.user.urls')),
    path('fruit/', include('mainapp.fruit.urls')),
    path('order/', include('orderapp.urls', namespace='order')),
    path('', fruit_list),

] + st(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')
]
