from django.urls import path

from orderapp import views

app_name = 'orderapp'

urlpatterns = [
    path('list', views.order_list, name='list')
]