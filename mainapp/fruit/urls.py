from django.urls import path

from mainapp.fruit.views import fruit_list, store, count_fruit

urlpatterns = [
    path('list', fruit_list),
    path('store', store),
    path('count', count_fruit)
]