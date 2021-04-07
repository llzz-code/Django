from django.urls import path
from mainapp.user.views import user_list3

urlpatterns = [
    path('list', user_list3),
]
