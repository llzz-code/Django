import os
from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
# Create your views here.
from django.template import loader
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt

from helloDjango import settings
from mainapp.models import UserEntity


def user_list(request):
    datas = [
        {'id': 101, 'name': 'lz'},
        {'id': 102, 'name': 'Tom'},
        {'id': 103, 'name': 'Jerry'},
    ]

    return render(request,
                  'user/list.html',
                  {
                      'users': datas,
                      'msg': '秀儿'
                  })

def user_list2(request):
    users = [
        {'id': 101, 'name': 'lz'},
        {'id': 102, 'name': 'Tom'},
        {'id': 103, 'name': 'Jerry'},
    ]
    msg = '秀儿'
    return render(request,
                  'user/list.html',
                  locals())
def user_list3(request):
    users = UserEntity.objects.all()
    msg = '秀儿'
    now = datetime.now()
    file_path = os.path.join(settings.BASE_DIR, r'mainapp\models.py')
    file_stat = os.stat(file_path)
    price = 19.235
    # # 加载模板
    # template = loader.get_template('user/list.html')
    #
    # # 渲染模板
    # html = template.render(context={
    #     'msg': msg,
    #     'users': users
    # })
    html = loader.render_to_string('user/list.html', locals())

    return HttpResponse(html, status=200)


# 局部取消csrf认证
@csrf_exempt
def login(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        if not all((name, password)):
            error_msg = '用户名或密码不可为空'
        else:
            qs = UserEntity.objects.filter(name=name)
            if qs.exists():
                login_user = qs.first()
                if check_password(password, login_user.password):
                    # 将登录用=用户信息存入session
                    request.session['login_user'] = {
                        'name': login_user.name,
                        'user_id': login_user.id,
                        'phone': login_user.phone
                    }

                    return redirect('/index')
                else:
                    error_mag = '密码错误'
            else:
                error_msg = '用户未注册，<a href="/user/register">去注册</a>'

    return render(request, 'user/login.html', locals())