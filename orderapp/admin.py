from django.contrib import admin

from mainapp.models import TagEntity
from orderapp.models import OrderEntity, CartEntity, FruitCartEntity


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'price', 'pay_status', 'pay_type', 'receiver', 'receiver_phone', 'receiver_address')
    fields = ('num', 'title', 'price', 'pay_status', 'pay_type', 'receiver', 'receiver_phone', 'receiver_address')
    list_filter = ('pay_status',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'no')

class FruitCartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'fruit', 'cnt', 'price1_title', 'price_title')

    def price_title(self, obj):
        return obj.price

    def price1_title(self, obj):
        return obj.price1
    price1_title.short_description = '单价'
    price_title.short_description = '小计'

class TagEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_num')
    fields = ('name', 'order_num')

admin.site.register(OrderEntity, OrderAdmin)
admin.site.register(CartEntity, CartAdmin)
admin.site.register(FruitCartEntity, FruitCartAdmin)
admin.site.register(TagEntity, TagEntityAdmin)