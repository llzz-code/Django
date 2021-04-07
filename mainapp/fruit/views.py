from django.shortcuts import render, redirect

from mainapp.models import FruitEntity, CateTypeEntity, StoreEntity


def fruit_list(request):
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

def store(request):
    stores = StoreEntity.objects.all()

    return render(request, 'fruit/list.html', locals())
