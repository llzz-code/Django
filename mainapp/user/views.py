from django.shortcuts import render
# Create your views here.
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
    return render(request,
                  'user/list.html',
                  locals())

