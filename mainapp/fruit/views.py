from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from mainapp.models import FruitEntity, CateTypeEntity, StoreEntity


def fruit_list(request):
    login_user = request.session.get('login_user', None)
    if login_user:

        # fruits = FruitEntity.objects.all()
        categories = CateTypeEntity.objects.all()
        stores = StoreEntity.objects.all()
        # 从查询参数中获取价格区间
        price1 = request.GET.get('price1', 0)
        price2 = request.GET.get('price2', 1000)
        if price1 == '':
            price1 = 0
        if price2 == '':
            price2 = 1000
        fruits = FruitEntity.objects.filter(price__gte=price1, price__lte=price2).all()
        # 根据价格区间查询满足条件的所有水果信息

        return render(request, 'fruit/list.html', locals())
    else:
        return redirect('/user/login')
def store(request):
    # 返回queryset对象的方法有
    # filter() exclude()  all()
    queryset = StoreEntity.objects.filter(crate_time__year__let=2002)
    first_store = queryset.first()    # 第一个对象

    # 如果是API接口，返回Json数据，可以用queryset.values()  返回QuerySet对象，对象迭代为字典  QuerySet<{}, {}>

    stores = queryset.all()
    return render(request, 'fruit/list.html', locals())

    # return JsonResponse(dict)   返回json响应


def count_fruit(request):
    # 返回json数据：统计每种分类的水果数量、最高价格、最低价格
    result = FruitEntity.objects.aggregate(cnt=Count('name'),
                                           max=Max('price'),
                                           min=Min('price'),
                                           avg=Avg('price'),
                                           sum=Sum('price'))
    # 全场水果打8.8折
    # FruitEntity.objects.update(price=F('price')*0.88)
    fruits = FruitEntity.objects.values()

    # Q操作 与& 或| 非~
    # 查询价格低于50的或大于100的
    fruits2 = FruitEntity.objects.filter(Q(price__lte=1) | Q(price__gte=100)).values()

    return JsonResponse({
        'count': result,
        'fruits': [fruit for fruit in fruits]
    })