from django.urls import path, re_path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('<str:cmd>', views.index, name='index'),
    #re_path(r'^<cmd>', views.index, name='index'),
]
