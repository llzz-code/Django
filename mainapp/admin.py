from django.contrib import admin
from mainapp.models import UserEntity, FruitEntity, CateTypeEntity, StoreEntity


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_per_page = 12    # 每页数据个数
    list_filter = ('id', 'phone')    # 过滤器(分类使用)
    search_fields = ('id', 'phone', 'name')    # 搜索

class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')

class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'price', 'category', 'summary')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id_', 'name', 'city', 'address', 'store_type', 'create_time', 'logo')
    fields = ('name', 'city', 'address', 'store_type', 'logo', 'summary')

# 将模型增加到站点中
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CateTypeEntity, CateTypeAdmin)
admin.site.register(FruitEntity, FruitAdmin)
admin.site.register(StoreEntity, StoreAdmin)

