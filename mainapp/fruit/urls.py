from django.urls import path

from mainapp.fruit.views import fruit_list, store

urlpatterns = [
    path('list', fruit_list),
    path('store', store)
]