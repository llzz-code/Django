from django.contrib import admin
from orderapp.models import OrderEntity, CartEntity, FruitCartEntity


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'price', 'pay_status', 'pay_type', 'receiver', 'receiver_phone', 'receiver_address')
    fields = ('num', 'title', 'price', 'pay_status', 'pay_type', 'receiver', 'receiver_phone', 'receiver_address')
    list_filter = ('pay_status',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'no')

class FruitCartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'fruit', 'cnt', 'price')


admin.site.register(OrderEntity, OrderAdmin)
admin.site.register(CartEntity, CartAdmin)
admin.site.register(FruitCartEntity, FruitCartAdmin)